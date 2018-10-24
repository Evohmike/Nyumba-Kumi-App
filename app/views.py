from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib import messages

from .models import *


from django.contrib.auth.decorators import login_required


@login_required(login_url = '/accounts/login')
def home(request):
    if Join.objects.filter(user_id = request.user).exists():
        hood = Neighbourhood.objects.get(pk = request.user.join.hood_id)    
        return render(request,'hood.html', locals())

    else:
        title = 'Nyumba-kumi'
        hoods = Neighbourhood.objects.all()
    
        return render(request,'home.html',locals())


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)
    return render(request,'profile.html',locals())

@login_required(login_url='/accounts/login/')
def createHood(request):
    if request.method == 'POST':
        form = CreateHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit = False)
            hood.user = request.user
            hood.save()
            messages.success(request, 'You Have succesfully created a hood.You may now join your neighbourhood')
            return redirect('home')
    else:
        form = CreateHoodForm()
        return render(request,'create.html',{"form":form})


@login_required(login_url='/accounts/login/')
def join(request , hoodid):

    this_hood = Neighbourhood.objects.get(pk = hoodid)
    if Join.objects.filter(user = request.user).exists():
        Join.objects.filter(user_id = request.user).update(hood_id = this_hood.id)
    else:
        Join(user=request.user, hood_id = this_hood.id).save()
    messages.success(request, 'Success! You have succesfully joined this Neighbourhood ')
    return redirect('home')



@login_required(login_url='/accounts/login/')
def exithood(request, id):
    Join.objects.get(user_id = request.user).delete()
    messages.error(request, "Neighbourhood exited")
    return redirect('home')

# @login_required(login_url='/accounts/login/')
# def createbusiness(request):
#     # if Join.objects.filter(user_id = request.user).exists():
#     #     print("user exist")
#     print(request.user.profile)
#     if request.method == 'POST':
#         form = CreateBizForm(request.POST)
#         if form.is_valid():
#             business = form.save(commit = False)
#             business.user = request.user
#             business.hood = request.user.profile.hood
#             business.save()
#             messages.success(request, 'Success! You have created a business')
#             return redirect('home')
#     else:
#         form = CreateBizForm()
#         return render(request, 'business.html', {"form":form})

@login_required(login_url='/accounts/login/')
def createbiz(request):
   
    hoods = Neighbourhood.objects.all()
    for hood in hoods:
        if Join.objects.filter(user_id = request.user).exists():
            if request.method == 'POST':
                form = CreateBizForm(request.POST)
                if form.is_valid():
                    business = form.save(commit = False)
                    business.user = request.user
                    business.hood = hood
                    business.save()
                    messages.success(request, 'Success! You have created a business')
                    return redirect('home')
            else:
                form = CreateBizForm()
                return render(request, 'business.html',{"form":form})
        else:
            messages.error(request, 'Error! Join a Neighbourhood to create a Business')


@login_required(login_url='/accounts/login/')
def createPost(request):
    hoods = Neighbourhood.objects.all()
    for hood in hoods:
        if Join.objects.filter(user_id = request.user).exists():
            if request.method == 'POST':
                form = CreatePostForm(request.POST)
                if form.is_valid():
                    post = form.save(commit = False)
                    post.user = request.user
                    post.hood = hood
                    post.save()
                    messages.success(request,'You have succesfully created a Forum Post')
                    return redirect('home')
            else:
                form = CreatePostForm()
                return render(request,'post.html',{"form":form})
        else:
            messages.error(request, 'Error! You can only create a post after Joining/Creating a neighbourhood')


# @login_required(login_url='/accounts/login/')
# def businesses(request):
#     biz = Business.objects.all()
#     return render(request,'hood.html',locals())


@login_required(login_url='/accounts/login/')
def search(request):

    if 'hood' in request.GET and request.GET["hood"]:
        search_term = request.GET.get("hood")
        searched_hoods = Neighbourhood.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"hood": searched_hoods})

    else:
        message = "You haven't searched for any hood"
        return render(request, 'search.html',{"message":message})



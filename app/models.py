from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length = 65)
    locations = (
        ('Umoja', 'Umoja'),
        ('kasarani', 'Kasarani'),
        ('Pangani', 'Pangani'),
        ('Roysambu', 'Roysambu'),
        ('Syokimau', 'Syokimau'),
        ('Kiambu', 'Kiambu'),
        ('karen', 'Karen'),
        ('Langata', 'Langata'),
        ('Buruburu', 'Buruburu')
    )
    loc  = models.CharField(max_length=65, choices=locations)
    hood_photo= models.ImageField(upload_to='images/', blank=True,)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Location'

    @classmethod
    def search_hood(cls, search_term):
        hoods = cls.objects.filter(name__icontains=search_term)
        return hoods

    def __str__(self):
        return f"{self.loc}"


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

class Profile(models.Model):
    name = models.CharField(max_length = 65, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hood = models.ForeignKey(Neighbourhood, blank=True, null=True)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    
    @classmethod
    def get_by_id(cls,id):
        profile = cls.objects.get(user = id)
        return profile

class Business(models.Model):
    name = models.CharField(max_length = 65)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbourhood,blank=True)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def get_biz(cls, hood):
        hoods = Business.objects.filter(hood_id=Neighbourhood)
        return hoods


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    hood = models.ForeignKey(Neighbourhood, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length = 65)
        
    def __str__(self):
        return self.description

class Join(models.Model):
    user_id = models.OneToOneField(User)
    hood_id = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.user_id



class Comments(models.Model):
    comment = models.CharField(max_length = 600)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment

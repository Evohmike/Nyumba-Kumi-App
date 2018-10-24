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
    description = models.TextField(default="My hood is the best")

    loc  = models.CharField(max_length=65, choices=locations)
    occupants = models.PositiveIntegerField()
    police = models.CharField(max_length=15, default='9999')
    health = models.CharField(max_length=15, default='071000000')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Location'

    @classmethod
    def search_by_title(cls,search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    def __str__(self):
        return self.name


    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hood = models.ForeignKey(Neighbourhood, blank=True, null=True)

    def __str__(self):
        return self.user.username


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    
    @classmethod
    def get_user_by_hood(cls, id):
        profile = Profile.objects.filter(hood_id=id).all()
        return profile


class Business(models.Model):
    name = models.CharField(max_length = 60)
    description = models.TextField(default="business")
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

    @classmethod
    def search_biz(cls, name):
        biz = cls.objects.filter(name__icontains=name)
        return biz


class Join(models.Model):
    user = models.OneToOneField(User)
    hood = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.user

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    hood = models.ForeignKey(Neighbourhood, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length = 65)
        
    def __str__(self):
        return self.description




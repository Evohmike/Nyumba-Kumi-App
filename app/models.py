from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
  Name = models.TextField(default="Anonymous")
  profile_pic = models.ImageField(upload_to='picture/', null=True, blank=True, default=0)
  bio = models.TextField(max_length=200, null=True, blank=True, default="my bio")
  # project = models.ForeignKey(Project, null=True)
  # hood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,related_name="neighbourhood",null=True,blank=True)

  

  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

  post_save.connect(create_user_profile, sender=User)

  def save_profile(self):
      self.save()

  def delete_profile(self):
      self.delete()

  @classmethod
  def search_users(cls, search_term):
      profiles = cls.objects.filter(user__username__icontains=search_term)
      return profiles


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Neighbourhood(models.Model):
    ESTATE_CHOICES = (
        ('Kiambu', 'Kiambu'),
        ('Kasarani', 'Kasarani'),
        ('Syokimau', 'Syokimau'),
        ('Makadara', 'Makadara'),
        ('Roysambu', 'Roysambu'),
        ('Umoja', 'Umoja'),
        ('Buruburu', 'Buruburu'), 
        ('Karen', 'Karen'),
        ('Lavington', 'Lavongton'),
        ('Kibera', 'Kibera'),

    )

    neighbourhood_name = models.CharField(max_length=30)
    neighbourhood_location = models.CharField(choices=ESTATE_CHOICES, max_length=200 ,default=0, null=True, blank=True)
    population= models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.neighbourhood_name

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood_by_id(cls, id):
        neighbourhoods = cls.objects.filter(pk=id)
        neighbourhoods.delete()

    @classmethod
    def get_neighbourhood_by_id(cls, id):
        neighbourhoods = cls.objects.get(pk=id)
        return neighbourhoods

    @classmethod
    def filter_by_location(cls, location):
        neighbourhoods = cls.objects.filter(location=location)
        return neighbourhoods

    @classmethod
    def search_neighbourhood(cls, search_term):
        neighbourhoods = cls.objects.filter(neighbourhood_name__icontains=search_term)
        return neighbourhoods

    @classmethod
    def update_neighbourhood(cls, id):
        neighbourhoods = cls.objects.filter(id=id).update(id=id)
        return neighbourhoods

    @classmethod
    def update_neighbourhood(cls, id):
        neighbourhoods = cls.objects.filter(id=id).update(id=id)
        return neighbourhoods







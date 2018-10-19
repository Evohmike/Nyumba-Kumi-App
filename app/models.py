from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
  profile_pic = models.ImageField(upload_to='picture/', null=True, blank=True, default=0)
  bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
  project = models.ForeignKey(Project, null=True)
  email= models.TextField(max_length=200, null=True, blank=True, default=0)
  neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,related_name="neighbourhood",null=True,blank=True)

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




class NeighbourHood(models.Model):




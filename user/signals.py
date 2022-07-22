from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from .models import Profile
from authentication.models import User


def create_profile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name = f'{user.first_name} {user.last_name}',
            email = user.email,
            phone_number = user.phone_number
        )

def deleteuser(sender,instance,**kwargs):
    user = instance.user
    user.delete()


def updateuser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profle.name
        user.email = profile.email
        user.phone_number = profile.phone_number



post_save.connect(create_profile, sender=User)
post_save.connect(updateuser, sender=Profile)
post_delete.connect(deleteuser, sender=Profile)
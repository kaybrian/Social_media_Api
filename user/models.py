from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.utils.translation import ugettext_lazy as _
from authentication.models import User
from cloudinary.models import CloudinaryField



class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=200)
    phone_number = PhoneNumberField(unique=True,null=True,blank=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = CloudinaryField('image')
    facebook_link =  models.CharField(max_length=200, null=True, blank=True)
    instagram_link =  models.CharField(max_length=200, null=True, blank=True)
    github_link =  models.CharField(max_length=200, null=True, blank=True)
    twitter_link =  models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
     


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='messages'
    )
    is_read = models.BooleanField(default=False, null=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from django.utils.translation import ugettext_lazy as _



class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("A user must have an email provided"))

        email = self.normalize_email(email)
        new_user = self.model(email=email,**extra_fields)
        new_user.set_password(password)

        new_user.save()
        return new_user


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Super User should have is_staff set to True "))

        if extra_fields.get('is_superuser') is not True:
                raise ValueError(_("Super User should have is_superuser set to True "))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Super User should have is_active set to True "))
        
        return self.create_superuser(email,password,**extra_fields)



class User(AbstractUser):
    username = models.CharField(max_length=50,null=True,blank=True)
    first_name = models.CharField(max_length=40,null=False,blank=False)
    last_name = models.CharField(max_length=40,null=False,blank=False)
    email = models.EmailField(unique=True,max_length=60)
    phone_number = PhoneNumberField(unique=True,null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','phone_number']

    def __str__(self):
        return str(self.first_name)
    


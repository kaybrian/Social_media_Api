from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _ 
from phonenumber_field.modelfields import PhoneNumberField



class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise valueError(_("A user must provide an email"))
        
        email = self.normalize_email(email)
        new_user = self.model(email,extre_fields)

        new_user.set_password(password)
        new_user.save()
        return new_user


    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff set to true"))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser should have is_superuser set to true"))

        if extra_fields.get('is_active') is not True:
            raise ValueError(_("Superuser should have is_active set to true"))

        return self.create_superuser(email,password,**extra_fields)



class User(AbstractUser):
    username = models.CharField(unique=True,max_length=30)
    email = models.EmailField(unique=True,max_length=50)
    phone_number = PhoneNumberField(null=False,unique=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username','phone_number']

    def __str__(self):
        return f"User -> {self.email} "
    

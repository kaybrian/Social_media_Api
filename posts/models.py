from django.db import models
from cloudinary.models import CloudinaryField
from user.models import Profile 
import uuid
from django.contrib.auth import get_user_model

# we are creating a user model
User = get_user_model()




class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, unique=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    image = CloudinaryField('image')
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.owner)
    
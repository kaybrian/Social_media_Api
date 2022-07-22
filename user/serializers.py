from .models import Profile  
from rest_framework import serializers 
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth import get_user_model

# we are creating a user model
User = get_user_model()



class ProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()
    id = serializers.UUIDField(read_only=True)
    user =serializers.CharField(read_only=True) 
    name =serializers.CharField(read_only=True) 
    email = serializers.EmailField(read_only=True) 
    phone_number = PhoneNumberField(read_only=True)
    created_at = serializers.DateTimeField()
        
    # serializer to hep return image urls from cloudnary 
    def get_profile_image(self, obj):
        if obj.profile_image:
            return obj.profile_image.url

    class Meta:
        model = Profile
        fields = ['id','user','name','email','phone_number','headline','bio','profile_image','facebook_link','instagram_link','github_link','twitter_link','created_at']

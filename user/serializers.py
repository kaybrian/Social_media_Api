from .models import Profile  
from rest_framework import serializers 
from phonenumber_field.serializerfields import PhoneNumberField



class PRofileSerializer(serializers.ModelSerializer):
    headline = serializers.CharField(max_length=25)
    bio = serializers.CharField(max_length=25)
    profile_image = serializers.CharField(max_length=25)
    facebook_link =  serializers.CharField(max_length=25)
    instagram_link =  serializers.CharField(max_length=25)
    github_link =  serializers.CharField(max_length=25)
    twitter_link =  serializers.CharField(max_length=25)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


    class Meta:
        model = Profile 
        fields = ['id','headline','bio','profile_image','facebook_link','instagram_link','github_link','twitter_link','created_at','updated_at']
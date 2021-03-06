from .models import Post 
from rest_framework import serializers 


class PostSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    owner = serializers.CharField(read_only=True)
    # serializer to hep return image urls from cloudnary 
    def get_image(self, obj):
        if obj.image:
            return obj.image.url

    class Meta:
        model = Post 
        fields = ['id','owner','description','image','likes','created_at','updated_at']

class PostDetialsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    owner = serializers.CharField(read_only=True)

    # serializer to hep return image urls from cloudnary 
    def get_image(self, obj):
        if obj.image:
            return obj.image.url

    class Meta:
        model = Post 
        fields = ['id','owner','description','image','likes','created_at','updated_at'] 
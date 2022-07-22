from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import generics,status 
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.contrib.auth import get_user_model

User= get_user_model()



class PostsListAPIView(generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self,request):
        posts = Post.objects.all().order_by('-created_at')
        serializer = self.serializer_class(instance=posts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

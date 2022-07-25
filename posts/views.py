from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response 
from rest_framework import generics,status 
from .serializers import PostSerializer,PostDetialsSerializer
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


    

class PostDetialView(generics.GenericAPIView):
    serializer_class = PostDetialsSerializer
    queryset = Post.objects.all()
    def get(self,request,pk):
        posts = get_object_or_404(Post,pk=pk)
        serializer = self.serializer_class(instance=posts)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self,request, pk):
        post = get_object_or_404(Post,pk=pk)
        owner = post.owner
        user = request.user

        if user == owner:
            serializer = self.serializer_class(instance=post)          

            if serializer.is_vaild():
                sserializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(data={"Message":"You aint allowed to perform this action"},status=status.HTTP_401_UNAUTHORIZED)

        

    
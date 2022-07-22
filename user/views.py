from django.shortcuts import render,get_object_or_404
from rest_framework import generics,status
from rest_framework.response import Response 
from . import serializers
from .models import Profile


class HelloProfile(generics.GenericAPIView):
    def get(self,request):
        return Response(data={
            "message":"Api is working well"
        },
        status=status.HTTP_200_OK
        )


class ProfileAPIView(generics.GenericAPIView):
    serializer_class = serializers.PRofileSerializer

    def get(self,request):
        user = request.user
        print(user)
        profile = get_object_or_404(Profile,user=user)
        print(profile)
        serializer = self.serializer_class(instance=profile)
        print(serializer)
        return Response(data=serializer.data,status=status.HTTP_200_OK)


        # return Response(data={
        #     "message":"it orked here now"
        # },status=status.HTTP_200_OK)
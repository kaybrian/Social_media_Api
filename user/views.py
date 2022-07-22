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
    serializer_class = serializers.ProfileSerializer
    def get(self,request):
        user = request.user
        profile = get_object_or_404(Profile,user=user)

        serializer = self.serializer_class(instance=profile)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        data = request.data

        profile = get_object_or_404(Profile,user=user)
        serializer = self.serializer_class(instance=profile)

        if serilalizer.is_valid():
            serilalizer.save()
            return Response(data=serilalizer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.data,status=status.HTTP_400_BAD_REQUEST)

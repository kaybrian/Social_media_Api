from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response



class HelloAuth(generics.GenericAPIView):
    def get(self,request):
        return Response(data={
            "Message":"Hello there its working"
        },status=status.HTTP_200_OK)




from django.urls import path 

from . import views 

urlpatterns = [
    path('welcome/',views.HelloProfile.as_view(),name="welcome_profile"),
    path('me/',views.ProfileAPIView.as_view(),name="profile"),
]

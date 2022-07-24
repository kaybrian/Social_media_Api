from django.urls import path 

from . import views 

urlpatterns = [
    path('welcome/',views.HelloProfile.as_view(),name="welcome_profile"),
    path('me/',views.ProfileAPIView.as_view(),name="my_profile"),
    path('update/me/',views.UpdateProfileDetails.as_view(),name="profile_update"),
    path('update-profile-image/me/',views.UpdateProfileImage.as_view(),name="update-profile-image"),
]

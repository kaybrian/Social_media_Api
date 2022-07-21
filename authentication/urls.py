from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.UserCreationAPIView.as_view(),name='signup')
]

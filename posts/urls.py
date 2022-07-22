from django.urls import path 
from  . import views 




urlpatterns = [
    path('newsfeed/',views.PostsListAPIView.as_view(),name="feed"),
    
]

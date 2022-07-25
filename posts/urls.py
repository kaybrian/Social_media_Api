from django.urls import path 
from  . import views 




urlpatterns = [
    path('newsfeed/',views.PostsListAPIView.as_view(),name="feed"),
    path('newsfeed/<str:pk>/',views.PostDetialView.as_view(),name="post"),
    
]

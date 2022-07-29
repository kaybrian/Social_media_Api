
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="School Social Media Application (Developed for fun)",
      default_version='v1',
      description="This is a social media API for a social network that i have build for fun, the main points of this app is to master custom uSer creation and other class based views in django rest framework.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="https://kayongo.herokuapp.com"),
      license=openapi.License(name="Open for use in anything you want "),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # django / swagger docs pages 
    path('swagger<format>.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # getting or using djoser for user creation 
    path('auth/', include('djoser.urls.jwt')),


    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('user/',include('user.urls')),
    path('feed/',include('posts.urls')),
]

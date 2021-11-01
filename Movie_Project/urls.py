"""Movie_Project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from MovieApp.views import ArtistsView,GenreView,MovieListView,MovieCRUDView
from rest_framework import routers

router=routers.DefaultRouter()
router.register('artists_manage',ArtistsView,basename='artists_manage')
router.register('genre_manage',GenreView,basename='genre_manage')
router.register('movielist',MovieListView,basename='movielist')
router.register('moviecrud',MovieCRUDView,basename='moviecrud')


from rest_framework.authtoken import views   #For Get/Generate token on client side in postman

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('get-api-token/',views.obtain_auth_token,name='get-api-token')
]

# username- xyz
# password- Xyz@12345

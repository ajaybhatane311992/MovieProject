from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import MovieListModel,GenreModel,ArtistsModel
from .serializers import MovieListSerializer,ArtistsSerializer,GenreSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Custom permissions import
from .permissions import IsReadOnly,IsGetOrPostOrPut,IsGetOrPost

# Create your views here.

class ArtistsView(ModelViewSet):
    queryset = ArtistsModel.objects.all()
    serializer_class = ArtistsSerializer
    authentication_classes = [TokenAuthentication]  # AuthToken use
    permission_classes = [IsAuthenticated,IsGetOrPost]

class GenreView(ModelViewSet):
    queryset = GenreModel.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsGetOrPost]

class MovieListView(ModelViewSet):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = [IsReadOnly]

'''
class MovieCRUDView(ModelViewSet):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsGetOrPostOrPut]
'''

class MovieCRUDView(ModelViewSet):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
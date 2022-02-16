from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import MovieListModel,GenreModel,ArtistsModel
from .serializers import MovieListSerializer,ArtistsSerializer,GenreSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly #IsAuthenticated,

# Custom permissions import
#from .permissions import IsReadOnly,IsGetOrPostOrPut,IsGetOrPost

# Create your views here.

'''
class ArtistsView(ModelViewSet):
    queryset = ArtistsModel.objects.all()
    serializer_class = ArtistsSerializer
    authentication_classes = [TokenAuthentication]  # AuthToken use
    permission_classes = [IsAuthenticatedOrReadOnly]    #permissions
    
'''

class ArtistsView(ModelViewSet):
#    queryset = ArtistsModel.objects.all()
    serializer_class = ArtistsSerializer
    authentication_classes = [TokenAuthentication]  # AuthToken use for secure
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return ArtistsModel.objects.all()



class GenreView(ModelViewSet):
    queryset = GenreModel.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class MovieCRUDView(ModelViewSet):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

'''
class MovieCRUDView(ModelViewSet):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsGetOrPostOrPut]
'''

'''
class MovieListView(ModelViewSet):
    queryset = MovieListModel.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = [IsReadOnly]
'''


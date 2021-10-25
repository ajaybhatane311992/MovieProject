from rest_framework.serializers import ModelSerializer
from .models import MovieListModel,ArtistsModel,GenreModel

class ArtistsSerializer(ModelSerializer):
    class Meta:
        model=ArtistsModel
        fields='__all__'

class GenreSerializer(ModelSerializer):
    class Meta:
        model=GenreModel
        fields='__all__'

class MovieListSerializer(ModelSerializer):
    class Meta:
        model=MovieListModel
        fields='__all__'






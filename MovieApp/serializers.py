from rest_framework.serializers import ModelSerializer
from .models import MovieListModel,ArtistsModel,GenreModel


class GenreSerializer(ModelSerializer):
    class Meta:
        model=GenreModel
        fields='__all__'



class ArtistsSerializer(ModelSerializer):
    #movieslist=MovieListSerializer(many=True,read_only=True)
    class Meta:
        model=ArtistsModel
        fields='__all__'

class MovieListSerializer(ModelSerializer):
    artists = ArtistsSerializer(read_only=True)
    genre= GenreSerializer(read_only=True)
    class Meta:
        model=MovieListModel
        fields='__all__'







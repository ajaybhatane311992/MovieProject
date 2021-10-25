from django.db import models

# Create your models here.
class ArtistsModel(models.Model):
    artists=models.CharField(max_length=20)
    def __str__(self):
        return self.artists

class GenreModel(models.Model):
    genre=models.CharField(max_length=20)
    def __str__(self):
        return self.genre

class MovieListModel(models.Model):
    movie_name=models.CharField(max_length=20)
    artists=models.ForeignKey(ArtistsModel,on_delete=models.CASCADE)
    genre=models.ForeignKey(GenreModel,on_delete=models.CASCADE)
    details=models.CharField(max_length=200)






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
    artists=models.ForeignKey(ArtistsModel,on_delete=models.CASCADE,related_name='movieslist')
    genre=models.ForeignKey(GenreModel,on_delete=models.CASCADE,related_name='genreby')
    details=models.CharField(max_length=200)

    def __str__(self):
        return self.movie_name






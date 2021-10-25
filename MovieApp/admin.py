from django.contrib import admin
from .models import ArtistsModel,GenreModel,MovieListModel

# Register your models here.
# For view in admin pannel

class ArtistsAdmin(admin.ModelAdmin):
    list_display = ['id','artists']
admin.site.register(ArtistsModel,ArtistsAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id','genre']
admin.site.register(GenreModel,GenreAdmin)

class MovieListAdmin(admin.ModelAdmin):
    list_display = ['id','movie_name','artists','genre','details']
admin.site.register(MovieListModel,MovieListAdmin)




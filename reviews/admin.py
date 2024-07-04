from django.contrib import admin
from .models import Movie, Review

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_movie_title', 'rating', 'comment')
    list_filter = ('movie',)
    list_display_links = ('id', 'user', 'get_movie_title', 'rating')

    def get_movie_title(self, obj):
        return obj.movie.title
    
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'release_date',)
    search_fields = ('title', 'description')
    list_display_links = ('id','title')
    list_filter = ('release_date',)
    ordering = ('release_date',)
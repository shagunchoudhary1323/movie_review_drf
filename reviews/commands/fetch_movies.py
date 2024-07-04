# reviews/management/commands/fetch_movies.py
import requests
from django.core.management.base import BaseCommand
from reviews.models import Movie

# class Command(BaseCommand):
#     help = 'Fetches movies from TMDb'

def handle(self, *args, **kwargs):
    api_key = 'e9097b137e5e9bacd6efb85111071284'
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'
    response = requests.get(url)
    movies = response.json().get('results', [])

    for movie in movies:
        Movie.objects.create(
            title=movie['title'],
            description=movie['overview'],
            release_date=movie['release_date']
        )

    self.stdout.write(self.style.SUCCESS('Successfully fetched movies'))

print(handle())
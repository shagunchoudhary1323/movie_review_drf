import requests
from django.core.management.base import BaseCommand
from reviews.models import Movie

class FetchMoviesCommand(BaseCommand):
    """Fetches movies from TMDb and creates them in the database."""

    def handle(self, request):
        api_key = "e9097b137e5e9bacd6efb85111071284" 
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status()  
            movies_data = response.json().get('results', [])

            for movie_data in movies_data:
                title = movie_data.get('title')
                description = movie_data.get('description', '')  
                release_date = movie_data.get('release_date', '')

                if title and release_date: 
                    Movie.objects.create(
                        title=title,
                        description=description,
                        release_date=release_date
                    )

            print(f'Successfully fetched {len(movies_data)} movies')

        except requests.exceptions.RequestException as e:
            print(f'Error fetching movies: {str(e)}')

if __name__ == '__main__':
    FetchMoviesCommand().execute()

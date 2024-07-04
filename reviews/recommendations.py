from django.db.models import Q, Avg
from .models import Movie, Review


class RecommendationSystem:
    @staticmethod
    def get_recommendations(user):

        if not user.is_authenticated:
            return Movie.objects.annotate(average_rating=Avg('review__rating')).order_by('-average_rating')[:5]

        rated_movies = Review.objects.filter(user=user).values_list('movie', flat=True)
        
        # Get similar users based on movie ratings
        similar_users = Review.objects.filter(
            movie__in=rated_movies
        ).exclude(user=user).values_list('user', flat=True).distinct()

        # Filter movies not rated by the user and get top 5 rated by similar users
        recommendations = Movie.objects.filter(
            ~Q(pk__in=rated_movies),
            pk__in=Review.objects.filter(user__in=similar_users).values_list('movie', flat=True)
        ).annotate(average_rating=Avg('review__rating')).order_by('-average_rating')[:5]

        return recommendations


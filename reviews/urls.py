from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    
    path('recommendations/', MovieRecommendationsView.as_view(), name='recommendations'),
    
    path('movie-search/', SearchMovieView.as_view(), name='movie-list'),
    path('review-search/', SearchReviewView.as_view(), name='review-list'),
]

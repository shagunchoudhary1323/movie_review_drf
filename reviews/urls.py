from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path("logout/", LogoutView.as_view(), name="logout"),
    
    path('reviews/', ReviewListCreateView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    
    path('recommendations/', MovieRecommendationsView.as_view(), name='recommendations'),
    
    path('search-movie/', SearchMovieView.as_view(), name='search_movie'),
    path('search-review/', SearchReviewView.as_view(), name='search_review'),
]

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Review, Movie
from .serializers import UserSerializer, MovieSerializer, ReviewSerializer
from .recommendations import RecommendationSystem
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.db.models import Q

class HomePageView(TemplateView):
    permission_classes = (AllowAny,)
    template_name = 'home.html'

class UserRegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": status.HTTP_201_CREATED,
                    "message": "User registered successfully!",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "User registration failed!",
                "data": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response(
            {
                "status":status.HTTP_200_OK,
                "message": "Logout successfully",
            },
            status=status.HTTP_200_OK,
        )


class MovieRecommendationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        movies = RecommendationSystem.get_recommendations(request.user)
        serializer = MovieSerializer(movies, many=True)
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "Recommendations retrieved successfully!",
                "data": serializer.data,
            }
        )

class ReviewListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "Reviews retrieved successfully!",
                "data": serializer.data,
            }
        )

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "status": status.HTTP_201_CREATED,
                    "message": "New review added!",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Review creation failed!",
                "data": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

class ReviewDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Review, pk=pk)

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": "Review retrieved successfully!",
                "data": serializer.data,
            }
        )

    def put(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "Review updated successfully!",
                    "data": serializer.data,
                }
            )
        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Review update failed!",
                "data": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(
            {
                "status": status.HTTP_204_NO_CONTENT,
                "message": "Review deleted successfully!",
                "data": None,
            },
            status=status.HTTP_204_NO_CONTENT,
        )

class SearchMovieView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        movies = Movie.objects.all()
        search_query = request.query_params.get('search', None)
        if search_query:
            movies = movies.filter(title__icontains=search_query) | movies.filter(description__icontains=search_query)

        if movies.exists():
            serializer = MovieSerializer(movies, many=True)
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "Movies Found successfully!",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "No similar movie found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
            
class SearchReviewView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        reviews = Review.objects.all()
        search_query = request.query_params.get('search', None)
        if search_query:
            reviews = reviews.filter(Q(comment__icontains=search_query))

        if reviews.exists():
            serializer = ReviewSerializer(reviews, many=True)
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": "Reviews found successfully!",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": "No similar reviews found!",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
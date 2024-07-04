from django.contrib.auth.models import User
from rest_framework import serializers
from django.db.models import Avg
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'average_rating']

    def get_average_rating(self, obj):
        return obj.review_set.aggregate(Avg('rating'))['rating__avg']
        
class ReviewSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')
    movie = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all())
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'comment', 'movie']
    
    def get_user(self, obj):
        return obj.user.username
    
    def get_movie(self, obj):
        return obj.movie.title

#from django.conf.auth import get_user_model
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')
    author_email = serializers.ReadOnlyField(source='author.email')
    author = AuthorSerializer
    class Meta:
        model = Post
        fields = [
            'pk',
            'username',
            'author',
            'author_email',
            'message',
            'created_at',
            'updated_at',
        ]

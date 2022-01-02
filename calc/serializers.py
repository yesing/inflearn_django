from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Post


class PostSerializer(ModelViewSet):
    class Meta:
        model = Post
        fields = '__all__'

        # m2 = serializers.IntegerField()
        # pyeong = serializers.IntegerField()

from rest_framework import serializers
from .models import Empty


class AddSerializer(serializers.ModelSerializer):
    val = serializers.SerializerMethodField()

    class Meta:
        model = Empty
        fields = ['val']

    @staticmethod
    def get_val(obj):
        return obj


class SubSerializer(serializers.ModelSerializer):
    val = serializers.SerializerMethodField()

    class Meta:
        model = Empty
        fields = ['val']

    @staticmethod
    def get_val(obj):
        return obj
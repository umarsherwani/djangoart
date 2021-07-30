from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, primary_key=True)
    email = serializers.EmailField(max_length=200)
    institution = serializers.CharField(max_length=70, blank=True)
    city = serializers.CharField(max_length=50, blank=True)
    country = serializers.CharField(max_length=25, blank=True)
    password = serializers.CharField(max_length=50)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.save()
        return instance
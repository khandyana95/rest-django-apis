from rest_framework import serializers
from profles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializer for the HelloApiView"""

    name = serializers.CharField(max_length=15)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for UserProfile"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password' : {
            'write_only' : True,
            'style' : {'input_type' : 'password'}
            }
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(email=validated_data.get('email'),
        name=validated_data.get('name'),
        password=validated_data.get('password')
        )

        return user


class UserProfileFeedSerializer(serializers.ModelSerializer):
    """Serializer for User Profile Feed"""

    class Meta:
        model = models.UserProfileFeed
        fields = ('id', 'user', 'status_text', 'created_on')
        extra_kwargs = {
            'user': {'read_only':True}
        }

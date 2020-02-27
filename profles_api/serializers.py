from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializer for the HelloApiView"""
    name = serializers.CharField(max_length=15)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profles_api import serializers


class HelloApiView(APIView):
    """API View for helloworld URL"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Get method"""
        context_data = [
            "This is HTTP get call",
            "This is from API View",
        ]

        return Response({"message":"Hello to REST Framework", "context_data": context_data})

    def post(self, request):
        """POST method"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """PUT method"""
        return Response({'message':'PUT'})

    def patch(self, request, pk=None):
        """PATCH method"""
        return Response({'message':'PATCH'})

    def delete(self, request, pk=None):
        """DELETE Method"""
        return Response({'message':'DELETE'})

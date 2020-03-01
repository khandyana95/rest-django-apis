from rest_framework import status, filters, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from profles_api import serializers, models, permissions


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


class HelloViewSet(viewsets.ViewSet):
    """ViewSet for Hello API"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Equivalent to GET in APIView"""
        context_data = [
            "This is an ViewSet",
            "Recommended for basic CRUD operations",
        ]

        return Response({"context_data":context_data})

    def create(self, request):
        """Equivalent to POST method"""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({"message":message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Equivalent to SEMI GET method"""
        return Response({"method":"RETRIEVE"})

    def update(self, request, pk=None):
        """Equivalent to PUT method"""
        return Response({"method":"UPDATE"})

    def partial_update(self, request, pk=None):
        """Equivalent to PATCH method"""
        return Response({"method":"PARTIAL UPDATE"})

    def destroy(self, request, pk=None):
        """Equivalent to DELETE method"""
        return Response({"method":"DESTROY"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ViewSet for Userprofile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnUserProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """"Login API view for Users"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Viewset for UserProfileFeed"""
    serializer_class = serializers.UserProfileFeedSerializer
    queryset = models.UserProfileFeed.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnUserProfileFeed, IsAuthenticatedOrReadOnly) #IsAuthenticated

    def perform_create(self, serializer):
        """To map the User Profile to Profile Feed"""
        serializer.save(user=self.request.user)

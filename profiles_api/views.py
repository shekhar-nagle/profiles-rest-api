from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
class HelloApiVIew(APIView):
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        an_api = [
        "Uses Statndard HTTP methods as function(get, post,put,delete)",

        "It is similar to traditional Django view",

        "Gives you control over ur application and logic",

        "It mapped manually to URL's"
        ]
        print("Log for ans_api",type(an_api))
        return Response({"message":"hello world", "an_api" : an_api})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        print("Log for serializer", type(serializer))
        if serializer.is_valid():
            name=serializer.validated_data.get("name")
            age=serializer.validated_data.get("age")
            message = f"hello {name, age}"
            return Response({'message' : message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)



    def put(self, request, pk=None):
        """Handling update an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handling partial update of an object """
        return Response({'method' : 'PATCH'})

    def delete(self, request,pk=None):
        """Delete an Object """
        return Response({'method' : 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet """
    serializer_class = serializers.HelloSerializers
    def list(self, request):
        """Return a hello Message """
        a_viewset = [
        "uses action such as (list, create, retrive, update, partial_update)",
        "Automatically map to URL's using routers",
        "Provides more functionality with less code"
        ]
        return Response({'message' : "Hello", 'a_viewset':a_viewset})
    def create(self,request):
        """create a new hello world message"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            age=serializer.validated_data.get('age')
            message=f'Hello{name, age}!'
            return Response({'message' : message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)
    def retrive(self, request, pk=None):
        """Handles getting an object by ID """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles update an object"""
        return Response({'http_method':'PUT'})
    def partial_update(self, request, pk=None):
        """Handles partial updates"""
        return Response({'http_method':'PATCH'})
    def destroy(self, request, pk=None):
        return Response({'http_method' : 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handling creating and updating profiles """
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    """To make it iterable we need tuple thats why comma else you will getting
    'type' object is not iterable error"""
class UserLoginApiViews(ObtainAuthToken):
    """Handle creating auth token """
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
    """To make ObtainAuthToken to be enable in browsable admin site
    and to make it visible in API site we have tp override it by using
    renderer_classes"""
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle create ,read, and update profile feed items"""
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedSerializer
    queryset=models.ProfileFeedItems.objects.all()
    def perform_create(self,serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

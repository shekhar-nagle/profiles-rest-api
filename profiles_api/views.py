from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
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

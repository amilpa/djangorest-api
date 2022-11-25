from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer , DatabaseFormat
from django.contrib.auth import login
from django.contrib.auth.models import User

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Create your views here.

@api_view(['GET'])
def getroutes(request):
    routes = [
            {
                'Endpoint' : '/collect',
                'method' : 'GET' , 
                'body' : None , 
                'description' : 'Returns an array of dictionaries',
                }
            ]
    return Response(routes)

@api_view(['GET'])
def getsupply(request):
    Data = WorkerManagement.objects.all()
    serializer = DatabaseFormat(Data ,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def additem(request):
    serializer = DatabaseFormat(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getitem(request , pk):
    item = WorkerManagement.objects.get(id = pk)
    serializer = DatabaseFormat(item , many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateitem(request , pk):
    data = request.data

    item = WorkerManagement.objects.get(id = pk)
    serializer = DatabaseFormat(item , data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteitem(request , pk):

    item = WorkerManagement.objects.get(id = pk)
    item.delete()
    return Response("Note is deleted")

@api_view(['GET'])
def getsupplyworker(request):
    Data = WorkerManagement.objects.all()
    serializer = DatabaseFormat(Data ,many = True)
    return Response(serializer.data)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)



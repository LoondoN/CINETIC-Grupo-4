from django.shortcuts import render
from Cinetic_App.models import *
from Cinetic_App.serializers import *
from rest_framework import viewsets,status
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
class User_view(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_Serializer

class Venta_view(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = Venta_Serializer

class Cust_view(viewsets.ModelViewSet):
    queryset = Cust.objects.all()
    serializer_class = Cust_Serializer

class Location_view(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = Location_Serializer

class Recibo_view(viewsets.ModelViewSet):
    queryset = Recibo.objects.all()
    serializer_class = Recibo_Serializer

class Sala_view(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = Sala_Serializer   

class Film_view(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = Film_Serializer

class Combo_view(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = Combo_Serializer

class Seat_view(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = Seat_Serializer

class Snack_view(viewsets.ModelViewSet):
    queryset = Snack.objects.all()
    serializer_class = Snack_Serializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if(token):
            token.delete()
            token, created = Token.objects.get_or_create(user=user)
        
        user.token = token.key
        user.save()
        usuario = User_Serializer(user)
        return Response(user.data)
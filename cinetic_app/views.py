from django.shortcuts import render
from cinetic_app.models import *
from cinetic_app.serializers import *
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create your views here.
class Usuario_view(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario


class Venta_view(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = Venta


class Cust_view(viewsets.ModelViewSet):
    queryset = Cust.objects.all()
    serializer_class = Cust


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
    serializer_class = Combo


class Seat_view(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = Seat


class Snack_view(viewsets.ModelViewSet):
    queryset = Snack.objects.all()
    serializer_class = Snack_Serializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if (token):
            token.delete()
            token, created = Token.objects.get_or_create(user=user)

        user.token = token.key
        user.save()
        usuarios = Usuario_Serializer(user)
        return Response(usuarios.data)

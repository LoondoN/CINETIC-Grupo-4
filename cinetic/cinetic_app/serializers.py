from asyncore import read, write
from copyreg import pickle
from dataclasses import fields
from importlib.resources import read_binary
from random import triangular
from rest_framework import serializers
from cinetic_app.models import *

class Usuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            telefono=validated_data['telefono'],
            direccion=validated_data['direccion'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            fecha_nacimiento=validated_data['fecha_nacimiento'],
            codigo_User=validated_data['codigo_User'],
            pseudonym_User=validated_data['pseudonym_User'],
            key_User=validated_data['key_User'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class Venta_Serializer(serializers.ModelSerializer):
    user = Usuario_Serializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Usuario.objects.all(),source='Usuario')
    class Meta:
        model = Venta
        fields = '__all__'

class  Cust_Serializer(serializers.ModelSerializer):
    venta = Venta_Serializer(read_only=True)
    venta_id =serializers.PrimaryKeyRelatedField(write_only=True,queryset=Venta.objects.all(),source='Venta')
    class Meta:
        model = Cust
        fields = '__all__'

class  Location_Serializer(serializers.ModelSerializer):
    venta = Venta_Serializer(read_only=True)
    venta_id =serializers.PrimaryKeyRelatedField(write_only=True,queryset=Venta.objects.all(),source='Venta')
    class Meta:
        model = Location
        fields = '__all__'

class Recibo_Serializer(serializers.ModelSerializer):
    venta = Venta_Serializer(read_only=True)
    venta_id =serializers.PrimaryKeyRelatedField(write_only=True,queryset=Venta.objects.all(),source='Venta')
    class Meta:
        model = Recibo
        fields = '__all__'

class Sala_Serializer(serializers.ModelSerializer):
    location = Location_Serializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Location.objects.all(),source='Location')
    class Meta:
        model = Sala
        fields = '__all__'

class Film_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class Combo_Serializer(serializers.ModelSerializer):
    recibo = Recibo_Serializer(read_only=True)
    recibo_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Recibo.objects.all(),source='Recibo')
    class Meta:
        model = Combo
        fields = '__all__'

class Seat_Serializer(serializers.ModelSerializer):
    sala = Sala_Serializer(read_only=True)
    sala_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Sala.objects.all(),source='Sala')
    location = Location_Serializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Location.objects.all(),source='Location')
    combo = Combo_Serializer(read_only=True)
    combo_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Combo.objects.all(),source='Combo')
    class Meta:
        model = Seat
        fields = '__all__'

class Snack_Serializer(serializers.ModelSerializer):
    combo = Combo_Serializer(read_only=True)
    combo_id =  serializers.PrimaryKeyRelatedField(write_only=True,queryset=Combo.objects.all(),source='Combo')
    class Meta:
        model = Snack
        fields = '__all__'
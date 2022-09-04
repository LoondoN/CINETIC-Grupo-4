from asyncore import read, write
from copyreg import pickle
from dataclasses import fields
from importlib.resources import read_binary
from random import triangular
from rest_framework import serializers
from Cinetic_App.models import *

class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            telefono=validated_data['telefono'],
            direccion=validated_data['direccion'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            fecha_nacimiento=validated_data['fecha_nacimiento'],
            Codigo_User=validated_data['Codigo_User'],
            pseudonym_User=validated_data['pseudonym_User'],
            key_User=validated_data['key_User'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class Venta_Serializer(serializers.ModelSerializer):
    User = User_Serializer(read_only=True)
    User_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=User.objects.all(),source='User')
    class Meta:
        model = Venta
        fields = '__all__'

class  Cust_Serializer(serializers.ModelSerializer):
    Venta = Venta_Serializer(read_only=True)
    Venta_id =serializers.PrimaryKeyRelatedField(write_only=True,queryset=Venta.objects.all(),source='Venta')
    class Meta:
        model = Cust
        fields = '__all__'

class  Location_Serializer(serializers.ModelSerializer):
    Venta = Venta_Serializer(read_only=True)
    Venta_id =serializers.PrimaryKeyRelatedField(write_only=True,queryset=Venta.objects.all(),source='Venta')
    class Meta:
        model = Location
        fields = '__all__'

class Recibo_Serializer(serializers.ModelSerializer):
    Venta = Venta_Serializer(read_only=True)
    Venta_id =serializers.PrimaryKeyRelatedField(write_only=True,queryset=Venta.objects.all(),source='Venta')
    class Meta:
        model = Recibo
        fields = '__all__'

class Sala_Serializer(serializers.ModelSerializer):
    Location = Location_Serializer(read_only=True)
    Location_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Location.objects.all(),source='Location')
    class Meta:
        model = Sala
        fields = '__all__'

class Film_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class Combo_Serializer(serializers.ModelSerializer):
    Recibo = Recibo_Serializer(read_only=True)
    Recibo_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Recibo.objects.all(),source='Recibo')
    class Meta:
        model = Combo
        fields = '__all__'

class Seat_Serializer(serializers.ModelSerializer):
    Sala = Sala_Serializer(read_only=True)
    Sala_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Sala.objects.all(),source='Sala')
    Location = Location_Serializer(read_only=True)
    Location_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Location.objects.all(),source='Location')
    Combo = Combo_Serializer(read_only=True)
    Combo_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Combo.objects.all(),source='Combo')
    class Meta:
        model = Seat
        fields = '__all__'

class Snack_Serializer(serializers.ModelSerializer):
    Combo = Combo_Serializer(read_only=True)
    Combo_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Combo.objects.all(),source='Combo')  
    class Meta:
        model = Snack
        fields = '__all__'

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    codigo_User  = models.CharField(max_length=100,unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=False,null=True)
    pseudonym_User = models.CharField(max_length=100)
    key_User = models.CharField(max_length=100)
    token = models.CharField(max_length=100, default='', null=True, blank=True)

class Venta(models.Model):
    codigo_Venta = models.CharField(max_length=100,unique=True)
    ticketDate_Venta = models.DateField(auto_now=False,null=True)
    totalPrice = models.CharField(max_length=1000)
    codigo_User = models.ForeignKey(Usuario,on_delete=models.PROTECT)

class Cust(models.Model):
    codigo_Cust = models.CharField(max_length=100, unique=True)
    name_Cust = models.CharField(max_length=100)
    lnames_Cust = models.CharField(max_length=100)
    tel_Cust = models.CharField(max_length=100)
    codigo_Venta = models.ForeignKey(Venta,on_delete=models.PROTECT)

class Location(models.Model):
    codigo_Loc = models.CharField(max_length=100, unique=True)
    name_Loc = models.CharField(max_length=100)
    city_Loc = models.CharField(max_length=100)
    email_Loc = models.CharField(max_length=100)
    tel_Loc = models.CharField(max_length=100)
    codigo_Venta = models.ForeignKey(Venta,on_delete=models.PROTECT)

class Recibo(models.Model):
    codigo_Rec = models.CharField(max_length=100, unique=True)
    date_Rec = models.DateField(auto_now_add=False, null=True)
    totalValue_Rec = models.CharField(max_length=100)
    codigo_Venta = models.ForeignKey(Venta,on_delete=models.PROTECT)

class Sala(models.Model):
    codigo_Sala = models.CharField(max_length=100, unique=True)
    name_Sala = models.CharField(max_length=100)
    price_Sala = models.CharField(max_length=100)
    quantity_Sala = models.CharField(max_length=100)
    layout_Sala = models.CharField(max_length=100)
    schedule_Sala = models.CharField(max_length=100)
    codigo_Loc = models.ForeignKey(Location, on_delete=models.PROTECT)

class Film(models.Model):
     codigo_Film = models.CharField(max_length=100, unique=True)
     name_Film = models.CharField(max_length=100)
     state_Film = models.CharField(max_length=100)
     class_Film = models.CharField(max_length=100)
     runningTime_Film = models.CharField(max_length=100)
     quality_Film = models.CharField(max_length=100)
     language_Film = models.CharField(max_length=100)
     dubbing_Film = models.CharField(max_length=100)

class Combo(models.Model):
    codigo_Combo = models.CharField(max_length=100, unique=True)
    products_Combo = models.CharField(max_length=100)
    price_Como = models.CharField(max_length=100)
    id_Rec = models.ForeignKey(Recibo,on_delete=models.PROTECT)

class Seat(models.Model):
    codigo_Seat = models.CharField(max_length=100, unique=True)
    row_Seat = models.IntegerField()
    column_Seat = models.IntegerField()
    state_Seat = models.CharField(max_length=100)
    codigo_Sala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    codigo_Loc = models.ForeignKey(Location, on_delete=models.PROTECT)
    codigo_Combo = models.ForeignKey(Combo, on_delete=models.PROTECT)

class Snack(models.Model):
    id_Snack = models.CharField(max_length=100, unique=True)
    name_Snack = models.CharField(max_length=100)
    synopsis_Snack = models.CharField(max_length=100)
    price_Snack = models.CharField(max_length=100)
    id_Combo = models.ForeignKey(Combo, on_delete=models.PROTECT)

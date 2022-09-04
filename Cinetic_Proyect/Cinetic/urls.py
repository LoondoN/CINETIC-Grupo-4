"""Cinetic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from Cinetic_App.views import *

router = routers.DefaultRouter()
router.register('user',User_view,basename='avion')
router.register('venta', Venta_view, basename='piloto')
router.register('cust', Cust_view, basename='tripulacion')
router.register('location', Location_view, basename='vuelo')
router.register('recibo', Recibo_view, basename='itinerario')
router.register('sala', Sala_view, basename='usuario')
router.register('film', Film_view, basename='film')
router.register('combo', Combo_view, basename='combo')
router.register('seat',Seat_view, basename='seat')
router.register('snack',Snack_view, basename='snack')

urlpatterns = [
    path('',include(router.urls)),
    path('token', CustomAuthToken.as_view(), name ='token'),
]

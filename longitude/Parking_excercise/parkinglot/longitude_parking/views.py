from longitude_parking.models import  Logitude_Latitude
from longitude_parking.models import Parking
from longitude_parking.serializer import LongitudeSerializer
from longitude_parking.serializer import ParkingSerializer
from django.shortcuts import render
from rest_framework import  generics

# Create your views here.
class ListLongitude(generics.ListCreateAPIView):
    queryset = Logitude_Latitude.objects.all()
    serializer_class = LongitudeSerializer


class ListParking(generics.ListCreateAPIView):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer


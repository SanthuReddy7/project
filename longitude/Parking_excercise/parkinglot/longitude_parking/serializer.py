from longitude_parking.models import  Logitude_Latitude
from longitude_parking.models import Parking
from rest_framework import  serializers


class LongitudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logitude_Latitude
        fields = ('id', 'name', 'address', 'longi' , 'lat', 'radius')


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ('id', 'parking_spot', 'time_range' )
from rest_framework import serializers
from .models import *

class GustSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gust
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["pk","reservation","name","mobile"]

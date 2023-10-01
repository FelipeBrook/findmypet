from rest_framework import serializers
from aplicacion.models import MascotaUser, RazaMascota

class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RazaMascota
        fields = '__all__'


class MascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MascotaUser
        fields = '__all__'
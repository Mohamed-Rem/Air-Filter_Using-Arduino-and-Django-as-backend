from rest_framework import serializers
from .models import Filter, SensorData, Technician, FilterManual

# Serializer pour Filter
class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'  # ou liste des champs ['filter_id','brand','status',...]

# Serializer pour SensorData
class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

# Serializer pour Technician
class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = '__all__'

# Serializer pour FilterManual
class FilterManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterManual
        fields = '__all__'

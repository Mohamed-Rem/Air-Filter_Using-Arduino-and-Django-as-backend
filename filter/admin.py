from django.contrib import admin

from django.contrib import admin
from .models import Filter, SensorData

admin.site.register(Filter)      # Permet de gérer les filtres dans l’admin
admin.site.register(SensorData)  # Permet de gérer les données capteurs

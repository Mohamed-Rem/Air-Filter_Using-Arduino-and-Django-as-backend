from django.db import models  # Import de la bibliothèque Django pour créer des modèles (tables)


# Modèle pour les filtres
class Filter(models.Model):  
    filter_id = models.AutoField(primary_key=True)  # Clé primaire
    brand = models.CharField(max_length=50)         # Nom de la marque
    install_date = models.DateTimeField()           # Date d’installation du filtre
    hours_used = models.IntegerField()              # Nombre d’heures d’utilisation
    status = models.CharField(max_length=20)        # État du filtre ("Clean", "Replace Soon", "Replace Now")

    def __str__(self):
        return f"{self.brand} (ID: {self.filter_id})"


# Modèle pour les données des capteurs
class SensorData(models.Model):  
    id = models.AutoField(primary_key=True)         # Clé primaire
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)  # Lien vers un filtre
    timestamp = models.DateTimeField()             # temps de la mesure
    temperature = models.FloatField()              # Température mesurée
    humidity = models.FloatField()                 # Humidité mesurée
    fan_speed = models.IntegerField()              # Vitesse du ventilateur

    def __str__(self):
        return f"Data for Filter {self.filter.filter_id} at {self.timestamp}"

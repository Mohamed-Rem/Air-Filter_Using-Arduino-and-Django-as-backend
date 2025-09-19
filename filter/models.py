from django.db import models  # Import de la bibliothèque Django pour créer des modèles (tables)


# Modele pour les filtres
class Filter(models.Model):  
    filter_id = models.AutoField(primary_key=True)  # Clé primaire
    brand = models.CharField(max_length=50)         # Nom de la marque
    install_date = models.DateTimeField()           # Date d’installation du filtre
    hours_used = models.IntegerField()              # Nombre d’heures d’utilisation
    status = models.CharField(max_length=20)        # État du filtre ("Clean", "Replace Soon", "Replace Now")

    def __str__(self):
        return f"{self.brand} (ID: {self.filter_id})"

# Modele pour filtre manuel
class FilterManual(models.Model):
    filter = models.OneToOneField(Filter, on_delete=models.CASCADE)  # Relation One-to-One (chaque filtre a un seul manuel d’utilisation)
    manual_text = models.TextField()  # Contenu du manuel
    language = models.CharField(max_length=50, default="English")  # Langue du manuel

    def __str__(self):
        return f"Manual for {self.filter.brand}"

# Modele pour les données des capteurs
class SensorData(models.Model):  
    id = models.AutoField(primary_key=True)         # Clé primaire
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)  # Relation One-to-Many (Plusieurs enregistrements appartiennent à un seul Filter)
    timestamp = models.DateTimeField()             # temps de la mesure
    temperature = models.FloatField()              # Température mesurée
    humidity = models.FloatField()                 # Humidité mesurée
    fan_speed = models.IntegerField()              # Vitesse du ventilateur

    def __str__(self):
        return f"Data for Filter {self.filter.filter_id} at {self.timestamp}"

# Modele pour les technichians
class Technician(models.Model):
    name = models.CharField(max_length=100)   # Nom de technician
    filters = models.ManyToManyField(Filter)  # Relation Many-to-Many (un technicien peut gérer plusieurs filtres, et un filtre peut être suivi par plusieurs techniciens)

    def __str__(self):
        return self.name

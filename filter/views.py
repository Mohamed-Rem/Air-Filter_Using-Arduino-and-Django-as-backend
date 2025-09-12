from django.http import HttpResponse 
from .models import Filter, SensorData             # importation de modèle Filter et SensorData

def home(request):  

    # Récupère tous les filtres et les données dans la base
    filters = Filter.objects.all()
    data = SensorData.objects.all()
    
    # Construit une réponse
    filters_output = ""
    for f in filters:
        filters_output += f"ID: {f.filter_id}, Brand: {f.brand},hours_used : {f.hours_used} hours, Status: {f.status}<br>"

    data_output = ""
    for d in data:
        data_output += f"Filter: {d.filter.brand}, Temperature: {d.temperature} C°, humidity: {d.humidity} %, fan_speed : {d.fan_speed}<br>"

    output = filters_output + "<br> <hr> <br>" + data_output
    
    return HttpResponse(output)  # Envoie le HTML au navigateur

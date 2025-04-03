# frontend/views.py
from django.shortcuts import render

def index(request):
    # Aquí podrías obtener o simular los datos de los sensores de Arduino
    datos_sensores = {
        'sensor1': 23.5,
        'sensor2': 45.2,
        'sensor3': 12.8,
    }
    return render(request, 'front/index.html', {'datos': datos_sensores})


from django.shortcuts import render, redirect
from .models import RegistrosPostura, HistoricoPostura, Alertas
from django.db.models import Max
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # Obtener el último registro de postura
    ultimo_registro = RegistrosPostura.objects.order_by('-timestamp').first()

    ultimo_dato = None
    if ultimo_registro:
        ultimo_dato = {
            'estado_postura': ultimo_registro.estado_postura,
            'nivel_respaldo': ultimo_registro.nivel_respaldo,
            'fecha': ultimo_registro.timestamp
        }

    # Obtener el historial reciente (últimos 10 cambios de postura)
    historico = HistoricoPostura.objects.select_related('registro').order_by('-timestamp')[:10]

    # Obtener las últimas alertas (últimas 10)
    alertas = Alertas.objects.select_related('registro').order_by('-timestamp')[:10]

    return render(request, 'index.html', {
        'ultimo_dato': ultimo_dato,
        'historico': historico,
        'alertas': alertas
    })




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # ✅ usamos el login de Django con alias
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')



@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

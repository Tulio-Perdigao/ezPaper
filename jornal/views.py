from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .forms import *
from .models import *

import re

# Create your views here.
def index(request):    
    return render(request, 'index.html', { 'active': 'index' })

def register(request):    
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                horario = form.cleaned_data['horario']

                hor = Horario.objects.get(id=horario.id)                

                if not set('#$"\'+={}[]%¨&*()/\\.,;?').intersection(username) and not set('@').intersection(username) and len(password) > 5 and hor:
                    user = Usuario.objects.create_user(username=username, email=email, password=password)
                    user.horario = horario
                    user.save()
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        if user.is_active:
                            return render(request, 'index.html', { 'active': 'index' }, status=201)
                    else:
                        return render(request, 'register.html', { 'active': 'register', "form": form }, status=500)
                else:
                    return render(request, 'register.html', { 'active': 'register', 'form': form, 'error_message': 'Dados inválidos!' }, status=400)
            else:
                return render(request, 'register.html', { 'active': 'register', 'form': form, 'error_message': 'Formulário inválido!' }, status=400)
        except Exception as e:
            print(e)
    else:
        return render(request, 'register.html', { 'active': 'register', "form": form }, status=200)    

def register_worktime(request):
    form = HorarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            horaInicio = form.cleaned_data['horaInicio']
            horaFim = form.cleaned_data['horaFim']

            horario = Horario()
            horario.horaInicio = horaInicio
            horario.horaFim = horaFim

            if horaInicio >= horaFim:
                return render(request, 'register_worktime.html', { 'active': 'register_worktime', "form": form, 'error_message': 'Horário inválido!' }, status=500)
            else:                
                if Horario.objects.filter(horaInicio=horaInicio, horaFim=horaFim).exists():
                    return render(request, 'register_worktime.html', { 'active': 'register_worktime', "form": form, 'error_message': 'Horário já cadastrado!' }, status=500)
                else:
                    horario.save()
                    if horario is not None:                        
                        return render(request, 'index.html', { 'active': 'index' }, status=201)
                    else:
                        return render(request, 'register_worktime.html', { 'active': 'register_worktime', "form": form }, status=500)
                    
    else:
        return render(request, 'register_worktime.html', { 'active': 'register_worktime', "form": form }, status=200)    

def user_list(request):
    users = Usuario.objects.all()
    return render(request, 'user_list.html', { 'active': 'user_list', 'users': users})

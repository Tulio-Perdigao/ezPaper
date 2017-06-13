from django.contrib.auth import login, authenticate
from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def index(request):    
    return render(request, 'index.html')

def register(request):
    form = UserForm(request.POST or None)    
    if request.method == 'POST':
        if form.is_valid():                
            username = form.cleaned_data['username']                
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            horario = form.cleaned_data['horario']
            
            user = Usuario.objects.create_user(username=username, email=email, password=password)                
            user.horario = horario
            print(horario)
            print(user.horario)
            user.save()
            user = authenticate(username=username, password=password)                
            if user is not None:
                if user.is_active:
                    return render(request, 'index.html')
            else:
                return render(request, 'index.html', { "form": form })
        else:
            return render(request, 'register.html', { 'form': form, 'error_message': 'Dados inválidos!' })
    else:
        return render(request, 'register.html', { "form": form })

    return render(request, 'register.html', { 'form': form })

def register_worktime(request):
    form = HorarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            horaInicio = form.cleaned_data['horaInicio']
            horaFim = form.cleaned_data['horaFim']

            horario = Horario()
            horario.horaInicio = horaInicio
            horario.horaFim = horaFim
            horario.save()

            if horario is not None:                
                return render(request, 'index.html')
            else:
                return render(request, 'register_worktime.html', { "form": form })    
    else:
        return render(request, 'register_worktime.html', { "form": form })

    return render(request, 'register_worktime.html', { 'form': form })

def user_list(request):
    users = Usuario.objects.all()
    return render(request, 'userlist.html', {'users': users})

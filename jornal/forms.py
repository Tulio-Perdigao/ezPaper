from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Usuário", max_length=50, min_length="3")    
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}), label="Email", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label="Senha", max_length=40)
    horario = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}), queryset=Horario.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'horario']

class HorarioForm(forms.ModelForm):
    horaInicio = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="Horário de início", max_length=2)
    horaFim = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), label="Horário de término", max_length=2)

    class Meta:
        model = Horario
        fields = ['horaInicio', 'horaFim']

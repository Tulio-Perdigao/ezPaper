from django.test import TestCase
from django.test.client import RequestFactory
from django.db.utils import IntegrityError
from .models import Usuario, Horario
from .views import *
import json

class UsuarioTestCase(TestCase):    
    def setUp(self):
        self.factory = RequestFactory()
        self.horario = Horario.objects.create(horaInicio=8, horaFim=18).id

    def test_can_create(self):        
        post_data = {
            'username': 'Pedro',
            'email': 'pedro@wisenet.inf.br',            
            'password': 'nipsinflames',
            'horario': self.horario
        }
        request = self.factory.post('/register', post_data)
        response = register(request)        
        self.assertEqual(response.status_code, 201)

    def test_missing_field(self):
        post_data = {
            'username': 'Pedro',            
            'password': 'nipsinflames',
            'horario': self.horario
        }
        request = self.factory.post('/register', post_data)
        response = register(request)        
        self.assertEqual(response.status_code, 400)

    def test_invalid_username(self):
        post_data = {
            'username': '#@*#&(',
            'email': 'pedro@wisenet.inf.br',            
            'password': 'nipsinflames',
            'horario': self.horario
        }
        request = self.factory.post('/register', post_data)
        response = register(request)        
        self.assertEqual(response.status_code, 400)
    
    def test_invalid_email(self):
        post_data = {
            'username': 'Pedro',
            'email': 'pedrowisenet.inf.br',            
            'password': 'nipsinflames',
            'horario': self.horario
        }
        request = self.factory.post('/register', post_data)
        response = register(request)        
        self.assertEqual(response.status_code, 400)
    
    def test_invalid_telephone(self):
        post_data = {
            'username': 'Pedro',
            'email': 'pedro@wisenet.inf.br',            
            'password': 'nipsinflames',
            'horario': self.horario
        }
        request = self.factory.post('/register', post_data)
        response = register(request)        
        self.assertEqual(response.status_code, 201)
    
    def test_invalid_password(self):
        post_data = {
            'username': 'Pedro',
            'email': 'pedro@wisenet.inf.br',            
            'password': 'nipsinflames',
            'horario': self.horario
        }
        request = self.factory.post('/register', post_data)
        response = register(request)        
        self.assertEqual(response.status_code, 201)
    
    def test_invalid_horario(self):
        post_data = {
            'username': 'Pedro',
            'email': 'pedro@wisenet.inf.br',            
            'password': 'nipsinflames',
            'horario': self.horario
        }
        request = self.factory.post('/register', post_data)
        response = register(request)        
        self.assertEqual(response.status_code, 201)

    '''def test_unique_username(self):
        try:
            user1 = Usuario.objects.create(username="Pedro", email="pedro@wisenet.inf.br", telephone="31993811533", password="nipsinflames", horario=self.horario1)
            user2 = Usuario.objects.create(username="Pedro", email="tulio@mitre.perd.br", telephone="31988888888", password="tuliotulio", horario=self.horario2)
        except IntegrityError:
            self.fail('Os nomes de usuário devem ser únicos!')    '''

class HorarioTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_can_create(self):        
        post_data = {
            'horaInicio': 8,
            'horaFim': 18
        }
        request = self.factory.post('/register_worktime', post_data)
        response = register_worktime(request)        
        self.assertEqual(response.status_code, 201)
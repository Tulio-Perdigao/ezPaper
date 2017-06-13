from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Usuario, Horario

class UsuarioTestCase(TestCase):    
    def setUp(self):
        self.horario1 = Horario.objects.create(horaInicio=8, horaFim=18)
        self.horario2 = Horario.objects.create(horaInicio=12, horaFim=22)

    def test_can_create(self):        
        user1 = Usuario.objects.create(username="Pedro", email="pedro@wisenet.inf.br", telephone="31993811533", password="nipsinflames", horario=self.horario1)
        user2 = Usuario.objects.create(username="Tulio", email="tulio@mitre.perd.br", telephone="31988888888", password="tuliotulio", horario=self.horario2)
        self.assertEqual(Usuario.objects.get(username="Pedro"), user1)
        self.assertEqual(Usuario.objects.get(username="Tulio"), user2)

    def test_unique_username(self):
        try:
            user1 = Usuario.objects.create(username="Pedro", email="pedro@wisenet.inf.br", telephone="31993811533", password="nipsinflames", horario=self.horario1)
            user2 = Usuario.objects.create(username="Pedro", email="tulio@mitre.perd.br", telephone="31988888888", password="tuliotulio", horario=self.horario2)
        except IntegrityError:
            self.fail('Os nomes de usuário devem ser únicos!')

    def test_telephone_number(self):
        try:
            tel = "xxxxxxxxxxx"
            user1 = Usuario.objects.create(username="Pedro", email="pedro@wisenet.inf.br", telephone=tel, password="nipsinflames", horario=self.horario1)
            int(tel)
        except ValueError:
            self.fail('O número de telefone deve conter apenas números!')

class HorarioTestCase(TestCase):
    def test_can_create(self):
        horario1 = Horario.objects.create(horaInicio=8, horaFim=18)
        horario2 = Horario.objects.create(horaInicio=12, horaFim=22)        
        self.assertEqual(Horario.objects.get(horaInicio=8, horaFim=18), horario1)
        self.assertEqual(Horario.objects.get(horaInicio=12, horaFim=22), horario2)
from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from ..models import MyModel
from ..forms import MyForm

class MyModelTestCase(TestCase):
    def setUp(self):
        """Configuração inicial para testes"""
        self.my_model = MyModel.objects.create(name="Teste", value=42)
    
    def test_model_creation(self):
        """Testa se o modelo foi criado corretamente"""
        self.assertEqual(self.my_model.name, "Teste")
        self.assertEqual(self.my_model.value, 42)
    
    def test_model_str_method(self):
        """Testa o método __str__ do modelo"""
        self.assertEqual(str(self.my_model), "Teste")

class MyViewTestCase(TestCase):
    def test_home_view_status_code(self):
        """Testa se a view inicial retorna status 200"""
        response = self.client.get(reverse('home'))  # Substitua 'home' pelo nome da sua URL
        self.assertEqual(response.status_code, 200)
    
    # def test_home_view_template_used(self):
    #     """Testa se a view inicial usa o template correto"""
    #     response = self.client.get(reverse('home'))
    #     self.assertTemplateUsed(response, 'home.html')  # Substitua 'home.html' pelo nome do template

# class MyFormTestCase(TestCase):
#     def test_valid_form(self):
#         """Testa um formulário válido"""
#         data = {'name': 'Teste', 'value': 42}
#         form = MyForm(data=data)
#         self.assertTrue(form.is_valid())
    
#     def test_invalid_form(self):
#         """Testa um formulário inválido"""
#         data = {'name': '', 'value': 42}  # Nome vazio
#         form = MyForm(data=data)
#         self.assertFalse(form.is_valid())


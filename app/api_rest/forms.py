from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'value']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o valor'}),
        }

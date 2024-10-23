from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Hospede, Locatario, Hotel, Lugar

# Formulário de criação de usuários (utilizado tanto por locatários quanto por hóspedes)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Formulário para cadastrar um hóspede
class HospedeForm(forms.ModelForm):
    class Meta:
        model = Hospede
        fields = ['nome_completo', 'email', 'telefone']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulário para cadastrar um locatário
class LocatarioForm(forms.ModelForm):
    class Meta:
        model = Locatario
        fields = ['nome_completo', 'email', 'telefone']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Formulário para cadastrar um hotel
class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['nome', 'localizacao', 'classificacao', 'link', 'locatario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
            'classificacao': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'locatario': forms.Select(attrs={'class': 'form-control'}),
        }

# Formulário para cadastrar um lugar
class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['preco', 'localizacao', 'categoria', 'descricao', 'link', 'classificacao', 'locatario']
        widgets = {
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'classificacao': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'locatario': forms.Select(attrs={'class': 'form-control'}),
        }

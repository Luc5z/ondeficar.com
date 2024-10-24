from django import forms
from .models import Hotel, Lugar
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['nome', 'localizacao', 'classificacao', 'link', 'foto', 'locatario']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Hotel'}),
            'localizacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localização'}),
            'classificacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Classificação'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Link do Hotel'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'locatario': forms.Select(attrs={'class': 'form-control'}),
        }

class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nome', 'preco', 'localizacao', 'categoria', 'descricao', 'link', 'classificacao', 'foto', 'locatario']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Nome do Lugar'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Preço'
            }),
            'localizacao': forms.TextInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Localização'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select mb-3'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Descrição', 
                'rows': 4
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Link do Lugar'
            }),
            'classificacao': forms.NumberInput(attrs={
                'class': 'form-control mb-3', 
                'placeholder': 'Classificação'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control mb-3'
            }),
            'locatario': forms.Select(attrs={
                'class': 'form-select mb-3'
            }),
        }



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a Senha'}),
        }

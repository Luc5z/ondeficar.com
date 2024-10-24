from django.contrib.auth.models import User
from django.db import models

class Hotel(models.Model):
    nome = models.CharField(max_length=255)  # Nome do hotel
    localizacao = models.CharField(max_length=255)  # Localização do hotel
    classificacao = models.DecimalField(max_digits=3, decimal_places=2)  # Classificação com duas casas decimais
    link = models.URLField()  # Link para o hotel
    locatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hoteis')  # Locatário que cadastrou o hotel
    foto = models.ImageField(upload_to='fotos_hoteis/', blank=True, null=True)  # Campo para foto do hotel

    def __str__(self):
        return self.nome

class Lugar(models.Model):
    CATEGORIA_CHOICES = [
        ('navio', 'Navio'),
        ('casa', 'Casa'),
        ('hotel', 'Hotel'),
    ]

    nome = models.CharField(max_length=255)  # Nome do lugar
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do lugar
    localizacao = models.CharField(max_length=255)  # Localização do lugar
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)  # Categoria (Navio, Casa, Hotel)
    descricao = models.TextField(blank=True, null=True)  # Descrição do lugar
    link = models.URLField()  # Link para o lugar
    classificacao = models.IntegerField()
    locatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lugares')  # Locatário que cadastrou o lugar
    foto = models.ImageField(upload_to='fotos_lugares/', blank=True, null=True)  # Campo para foto do lugar

    def __str__(self):
        return f'{self.categoria.capitalize()} - {self.localizacao}'

from django.contrib.auth.models import User
from django.db import models

class Hotel(models.Model):
    nome = models.CharField(max_length=255)  # Nome do hotel
    localizacao = models.CharField(max_length=255)  # Localização do hotel
    classificacao = models.DecimalField(max_digits=3, decimal_places=2)  # Classificação com duas casas decimais
    link = models.URLField()  # Link para o hotel
    locatario = models.ForeignKey('Locatario', on_delete=models.CASCADE, related_name='hoteis')  # Locatário que cadastrou o hotel
    foto = models.ImageField(upload_to='fotos_hoteis/', blank=True, null=True)  # Campo para foto do hotel

    def __str__(self):
        return self.nome

class Lugar(models.Model):
    CATEGORIA_CHOICES = [
        ('navio', 'Navio'),
        ('casa', 'Casa'),
        ('hotel', 'Hotel'),
    ]

    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do lugar
    localizacao = models.CharField(max_length=255)  # Localização do lugar
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)  # Categoria (Navio, Casa, Hotel)
    descricao = models.TextField()  # Descrição do lugar
    link = models.URLField()  # Link para o lugar
    classificacao = models.DecimalField(max_digits=3, decimal_places=2)  # Classificação com duas casas decimais
    locatario = models.ForeignKey('Locatario', on_delete=models.CASCADE, related_name='lugares')  # Locatário que cadastrou o lugar
    foto = models.ImageField(upload_to='fotos_lugares/', blank=True, null=True)  # Campo para foto do lugar

    def __str__(self):
        return f'{self.categoria.capitalize()} - {self.localizacao}'

class Locatario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Ligação com o usuário Django padrão
    nome_completo = models.CharField(max_length=255)  # Nome completo do locatário
    email = models.EmailField()  # Email do locatário
    telefone = models.CharField(max_length=20, blank=True, null=True)  # Telefone do locatário (opcional)

    def __str__(self):
        return self.nome_completo

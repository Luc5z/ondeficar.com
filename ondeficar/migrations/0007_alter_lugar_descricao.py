# Generated by Django 5.1.2 on 2024-10-24 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ondeficar', '0006_alter_lugar_classificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]

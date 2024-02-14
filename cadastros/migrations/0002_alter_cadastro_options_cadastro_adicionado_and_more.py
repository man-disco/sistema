# Generated by Django 5.0.1 on 2024-01-26 22:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastro',
            options={'verbose_name_plural': 'Cadastros'},
        ),
        migrations.AddField(
            model_name='cadastro',
            name='adicionado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='alterado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-08 00:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_alter_cadastro_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='alterado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_instances', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='criado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_instances', to=settings.AUTH_USER_MODEL),
        ),
    ]

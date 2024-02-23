# Generated by Django 5.0.1 on 2024-02-21 04:54

import core.storage_backends
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='contract',
            field=models.FileField(null=True, storage=core.storage_backends.PrivateMediaStorage, upload_to='contratos/', verbose_name='Contrato'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='document',
            field=models.FileField(blank=True, storage=core.storage_backends.PrivateMediaStorage, upload_to='boletos/', verbose_name='Boleto'),
        ),
    ]
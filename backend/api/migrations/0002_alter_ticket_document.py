# Generated by Django 5.0.1 on 2024-02-19 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='document',
            field=models.FileField(blank=True, upload_to='boletos/', verbose_name='Boleto'),
        ),
    ]

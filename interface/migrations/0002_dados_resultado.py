# Generated by Django 5.0.2 on 2024-02-09 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados',
            name='resultado',
            field=models.FloatField(default=0),
        ),
    ]
# Generated by Django 5.1.7 on 2025-04-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heallthApp', '0003_service_description_en_service_description_sq_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='description_en',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='description_sq',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]

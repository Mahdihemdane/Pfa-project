# Generated by Django 5.0.6 on 2024-06-08 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisateur',
            name='categorie',
            field=models.CharField(choices=[('ligue 1', 'ligue 1'), ('ligue 2', 'ligue 2'), ('Coupe de tunisie', 'Coupe de tunisie'), ('Amateur ligue', 'Amateur ligue')], max_length=255),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='reps',
            field=models.CharField(blank=True, max_length=50, verbose_name='Reps (e.g., 10kg x 12)'),
        ),
    ]

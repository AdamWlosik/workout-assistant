# Generated by Django 5.0.6 on 2024-06-13 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_exercise_reps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='reps',
        ),
    ]

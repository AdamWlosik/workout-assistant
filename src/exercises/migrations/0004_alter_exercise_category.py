# Generated by Django 5.0.6 on 2024-06-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_remove_exercise_reps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='category',
            field=models.CharField(choices=[('1', 'Chest'), ('2', 'Back'), ('3', 'Triceps'), ('4', 'Forearm'), ('5', 'Legs'), ('6', 'Shoulders'), ('7', 'Biceps'), ('8', 'ABS'), ('9', 'Glutes'), ('10', 'Necks'), ('11', 'Warm Up'), ('12', 'Cardio'), ('13', 'Core')], max_length=100),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-13 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_remove_exercise_reps'),
        ('trainings', '0006_alter_training_exercises'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainingexercise',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='trainingexercise',
            unique_together={('training', 'exercise')},
        ),
    ]
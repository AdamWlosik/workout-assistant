# Generated by Django 5.0.6 on 2024-06-13 11:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_exercise_reps'),
        ('trainings', '0004_alter_training_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='exercises',
        ),
        migrations.CreateModel(
            name='TrainingExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.CharField(blank=True, max_length=50, verbose_name='Reps (e.g., 10kg x 12)')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.exercise')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.training')),
            ],
            options={
                'verbose_name': 'Training Exercise',
                'verbose_name_plural': 'Training Exercises',
            },
        ),
        migrations.AddField(
            model_name='training',
            name='exercises',
            field=models.ManyToManyField(through='trainings.TrainingExercise', to='exercises.exercise', verbose_name='Exercises'),
        ),
    ]

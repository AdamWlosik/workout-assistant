# Generated by Django 5.0.6 on 2024-12-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0023_alter_trainingexercise_event_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingexercise',
            name='event_id',
        ),
        migrations.AddField(
            model_name='trainingexercise',
            name='training_exercise_event_id',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
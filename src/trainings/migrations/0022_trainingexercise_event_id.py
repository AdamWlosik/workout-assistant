# Generated by Django 5.0.6 on 2024-12-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0021_alter_trainingexercise_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingexercise',
            name='event_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

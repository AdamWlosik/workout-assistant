# Generated by Django 5.0.6 on 2024-06-02 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainings',
            name='training_date',
        ),
    ]

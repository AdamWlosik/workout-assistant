# Generated by Django 5.0.6 on 2024-06-17 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendary', '0006_alter_event_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_time',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
    ]

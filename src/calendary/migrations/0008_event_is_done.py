# Generated by Django 5.0.6 on 2024-12-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendary', '0007_rename_end_time_event_date_remove_event_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
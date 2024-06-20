# Generated by Django 5.0.6 on 2024-06-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendary', '0003_rename_start_date_event_start_time'),
        ('trainings', '0011_category_training_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='trainings',
            field=models.ManyToManyField(blank=True, related_name='events', to='trainings.training', verbose_name='Training'),
        ),
    ]
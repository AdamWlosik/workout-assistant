# Generated by Django 5.0.6 on 2024-06-13 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0009_remove_category_name_category_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='training',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
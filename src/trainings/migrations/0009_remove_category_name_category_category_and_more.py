# Generated by Django 5.0.6 on 2024-06-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0008_category_remove_training_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('1', 'Chest'), ('2', 'Back'), ('3', 'Triceps'), ('4', 'Forearm'), ('5', 'Legs'), ('6', 'Shoulders'), ('7', 'Biceps'), ('8', 'ABS'), ('9', 'Glutes'), ('10', 'Necks'), ('11', 'Warm Up'), ('12', 'Cardio')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='training',
            name='category',
            field=models.ManyToManyField(blank=True, default='', to='trainings.category', verbose_name='Category'),
        ),
    ]

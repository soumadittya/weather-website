# Generated by Django 3.0 on 2020-03-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_image_theme_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_theme',
            name='image_theme_id',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
# Generated by Django 3.0 on 2020-03-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200325_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_theme',
            name='image_theme',
            field=models.ImageField(blank=True, upload_to='images_theme'),
        ),
    ]
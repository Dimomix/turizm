# Generated by Django 4.1.4 on 2023-03-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turist', '0010_alter_tour_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]

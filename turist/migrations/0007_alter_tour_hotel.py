# Generated by Django 4.1.4 on 2023-03-05 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turist', '0006_alter_hotel_image_alter_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='turist.hotel'),
        ),
    ]
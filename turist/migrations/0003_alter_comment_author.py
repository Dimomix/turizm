# Generated by Django 4.1.4 on 2023-03-05 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turist', '0002_alter_city_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turist.user'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-03-05 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='employees',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'verbose_name': 'Отель', 'verbose_name_plural': 'Отели'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterModelOptions(
            name='tour',
            options={'verbose_name': 'Тур', 'verbose_name_plural': 'Туры'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='way',
            options={'verbose_name': 'Транспорт', 'verbose_name_plural': 'Транспорты'},
        ),
    ]
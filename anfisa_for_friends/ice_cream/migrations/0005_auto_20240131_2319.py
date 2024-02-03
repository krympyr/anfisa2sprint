# Generated by Django 3.2.16 on 2024-01-31 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0004_auto_20240131_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icecream',
            name='title',
            field=models.CharField(help_text='Уникальное название мороженого, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='title',
            field=models.CharField(help_text='Уникальное название топпинга, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёртки, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
    ]
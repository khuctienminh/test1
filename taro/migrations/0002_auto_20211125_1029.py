# Generated by Django 2.2.2 on 2021-11-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taro',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='写真１'),
        ),
        migrations.AlterField(
            model_name='taro',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='写真２'),
        ),
        migrations.AlterField(
            model_name='taro',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='写真３'),
        ),
    ]
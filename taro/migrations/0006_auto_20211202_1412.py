# Generated by Django 2.2.2 on 2021-12-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taro', '0005_auto_20211201_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='taro',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='写真４'),
        ),
        migrations.AddField(
            model_name='taro',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='写真５'),
        ),
    ]

# Generated by Django 2.2.2 on 2022-01-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20220114_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='static/assets/img/anhdefault.jpg', null=True, upload_to='images', verbose_name='写真'),
        ),
    ]
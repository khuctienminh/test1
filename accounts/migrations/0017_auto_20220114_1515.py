# Generated by Django 2.2.2 on 2022-01-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20220114_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='images/anhdefault.jpg', null=True, upload_to='images', verbose_name='写真'),
        ),
    ]

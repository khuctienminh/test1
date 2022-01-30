# Generated by Django 2.2.2 on 2022-01-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taro', '0006_auto_20211202_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taro',
            name='kenmei',
            field=models.CharField(choices=[('chiba', '千葉'), ('kanagawa', '神奈川'), ('tokyo', '東京'), ('oosaka', '大阪')], default=0, max_length=40, verbose_name='都道府県'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='taro',
            name='okane',
            field=models.IntegerField(default=0, verbose_name='料金'),
            preserve_default=False,
        ),
    ]

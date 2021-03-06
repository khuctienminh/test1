# Generated by Django 2.2.2 on 2021-11-25 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tagname', models.CharField(max_length=40, verbose_name='施設名')),
            ],
            options={
                'verbose_name_plural': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Taro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaname', models.CharField(max_length=40, verbose_name='施設名')),
                ('eki', models.CharField(max_length=40, verbose_name='駅')),
                ('kenmei', models.CharField(blank=True, choices=[('chiba', '千葉'), ('kanagawa', '神奈川'), ('tokyo', '東京'), ('oosaka', '大阪')], max_length=40, null=True, verbose_name='都道府県')),
                ('okane', models.IntegerField(blank=True, null=True, verbose_name='料金')),
                ('naiyou', models.TextField(max_length=800, verbose_name='内容')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真１')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真２')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真３')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='新日時')),
                ('tag', models.ManyToManyField(to='taro.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Taro',
            },
        ),
    ]

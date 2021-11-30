# Generated by Django 2.2.2 on 2021-11-19 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211119_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='sex',
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(choices=[(10, '10代'), (20, '20代'), (30, '30代'), (40, '40代'), (50, '50代'), (60, '60代'), (70, '70代'), (80, '80代'), (90, '90代')], verbose_name='年代')),
                ('sex', models.CharField(choices=[('man', '男性'), ('female', '女性')], max_length=40, verbose_name='性別')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
            options={
                'verbose_name_plural': 'Userinfo',
            },
        ),
    ]

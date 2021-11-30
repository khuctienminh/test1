# Generated by Django 2.2.2 on 2021-11-19 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20211117_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, choices=[(10, '10代'), (20, '20代'), (30, '30代'), (40, '40代'), (50, '50代'), (60, '60代'), (70, '70代'), (80, '80代'), (90, '90代')], null=True, verbose_name='年代'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='sex',
            field=models.CharField(blank=True, choices=[('man', '男性'), ('female', '女性')], max_length=40, null=True, verbose_name='性別'),
        ),
        migrations.DeleteModel(
            name='Userinfo',
        ),
    ]
# Generated by Django 2.2.2 on 2022-01-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_customuser_shokai'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='名前'),
        ),
    ]
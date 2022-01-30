from re import T
from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import widgets
# Create your models here.

YEAR_CHOICES = (
        (10, '10代'),
        (20, '20代'),
        (30, '30代'),
        (40, '40代'),
        (50, '50代'),
        (60, '60代'),
        (70, '70代'),
        (80, '80代'),
        (90, '90代'),
        (100, '100以上'),
    )

Sex_choice = (
  ('男性','男性'),
  ('女性','女性'),
)

class CustomUser(AbstractUser):

  age = models.IntegerField(verbose_name='年代', choices=YEAR_CHOICES,blank=True,null=True)
  sex = models.CharField(verbose_name='性別',choices=Sex_choice,max_length=40,blank=True,null=True)
  image = models.ImageField(verbose_name='写真',upload_to='images',blank=True,null=True,default='images/default.png')
  shokai = models.TextField(verbose_name='紹介',blank=True,null=True)
  likerecieve = models.IntegerField(verbose_name='いいね数',default=0)

  
  class Meta:
    verbose_name_plural ='CustomUser'
    

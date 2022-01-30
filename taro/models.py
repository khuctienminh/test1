from django.db import models
from django.db.models.aggregates import Max
from accounts.models import CustomUser
from django.db.models import Count
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.


Ken_choice = (
  ('千葉県','千葉県'),
  ('神奈川県','神奈川県'),
  ('東京県','東京県'),
  ('大阪県','大阪県'),
)

class Tag(models.Model):
  id = models.AutoField(primary_key=True)
  tagname =models.CharField(verbose_name='タグ',max_length=40)

  class Meta:
        verbose_name_plural = 'Tag'
  def __str__(self):
        return self.tagname




class Taro(models.Model):

    user = models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT,related_name='posts')
    areaname= models.CharField(verbose_name='施設名',max_length=40)
    eki = models.CharField(verbose_name='駅',max_length=40)
    kenmei = models.CharField(verbose_name='都道府県',max_length=40,choices=Ken_choice,blank=True,null=True)
    okane = models.IntegerField(verbose_name='料金',blank=True,null=True,validators=[MinValueValidator(0), MaxValueValidator(100000)])
    tag = models.ManyToManyField(Tag)
    naiyou = models.TextField(verbose_name='内容',max_length=800)
    photo1 = models.ImageField(verbose_name='写真１',upload_to='images',blank=True,null=True)
    photo2 = models.ImageField(verbose_name='写真２',upload_to='images',blank=True,null=True)
    photo3 = models.ImageField(verbose_name='写真３',upload_to='images',blank=True,null=True)
    photo4 = models.ImageField(verbose_name='写真４',upload_to='images',blank=True,null=True)
    photo5 = models.ImageField(verbose_name='写真５',upload_to='images',blank=True,null=True)
    likes = models.ManyToManyField(CustomUser,related_name='likes')
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='新日時',auto_now=True)
    likestotal = models.IntegerField(verbose_name='postいいね数',default=0)

    def total_likes(self):
      return self.likes.count()
    
    

    class Meta:
        verbose_name_plural = 'Taro'
    def __str__(self):
        return self.areaname


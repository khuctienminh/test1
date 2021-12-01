from django.db import models
from accounts.models import CustomUser
from django.db.models import Count
# Create your models here.


Ken_choice = (
  ('chiba','千葉'),
  ('kanagawa','神奈川'),
  ('tokyo','東京'),
  ('oosaka','大阪'),
)

class Tag(models.Model):
  id = models.AutoField(primary_key=True)
  tagname =models.CharField(verbose_name='施設名',max_length=40)

  class Meta:
        verbose_name_plural = 'Tag'

class Taro(models.Model):

    user = models.ForeignKey(CustomUser,verbose_name='ユーザー',on_delete=models.PROTECT,related_name='posts')
    areaname= models.CharField(verbose_name='施設名',max_length=40)
    eki = models.CharField(verbose_name='駅',max_length=40)
    kenmei = models.CharField(verbose_name='都道府県',max_length=40,choices=Ken_choice,blank=True,null=True)
    okane = models.IntegerField(verbose_name='料金',blank=True,null=True)
    tag = models.ManyToManyField(Tag)
    naiyou = models.TextField(verbose_name='内容',max_length=800)
    photo1 = models.ImageField(verbose_name='写真１',upload_to='images',blank=True,null=True)
    photo2 = models.ImageField(verbose_name='写真２',upload_to='images',blank=True,null=True)
    photo3 = models.ImageField(verbose_name='写真３',upload_to='images',blank=True,null=True)
    likes = models.ManyToManyField(CustomUser,related_name='likes')
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='新日時',auto_now=True)

    def total_likes(self):
      return self.likes.count()

    class Meta:
        verbose_name_plural = 'Taro'


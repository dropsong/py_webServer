from django.db import models

# Create your models here.

from datetime import datetime
class Comment(models.Model):
    email=models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

# 酒店预订、入住日期、离开日期
class Event(models.Model):
    description = models.CharField(max_length=100)
    start = models.DateTimeField()
    finish = models.DateTimeField()

# 酒店预订、姓名、房间号、日期
class Event1(models.Model):
    name = models.CharField(max_length=50)
    room_number = models.IntegerField()
    date = models.DateField()

class Account(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('auth.User',related_name='accounts',on_delete=models.CASCADE,default=None,db_constraint=False)



# 唱片和歌曲的模型类
class Album(models.Model):  # 唱片
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name

class Track(models.Model):  # 歌曲
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
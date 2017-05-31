# -*- encoding:utf-8 -*-
from django.db import models
from datetime import datetime

from users.models import UserInfo

# Create your models here.
class News(models.Model):
    userinfo    = models.ForeignKey(UserInfo, verbose_name=u"用户")
    title       = models.CharField(max_length=200, verbose_name=u"标题")
    summary     = models.TextField(verbose_name=u"摘要")
    thumbnail   = models.ImageField(upload_to="thumbnail/%Y/%m", verbose_name=u"缩略图", max_length=100)
    add_time    = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"新闻"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title
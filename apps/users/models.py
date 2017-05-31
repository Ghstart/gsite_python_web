# -*- encoding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class UserInfo(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    mobile    = models.CharField(max_length=11, verbose_name=u"手机号码")
    avatar    = models.ImageField(upload_to="avatar/%Y/%m", default="avatar/default.png", max_length=100)
    add_time  = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

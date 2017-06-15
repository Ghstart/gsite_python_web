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

class jobbole_date(models.Model):
    custom_description = models.CharField(max_length=200, verbose_name=u"自我描述")
    detail_info_url    = models.URLField(max_length=300, verbose_name=u"详情链接")
    detail_info_url_object_id = models.CharField(max_length=50, verbose_name=u"链接的加密")
    publish_time       = models.CharField(max_length=45, verbose_name=u"发布时间")
    location           = models.CharField(max_length=45, verbose_name=u"发布地址")
    fav_num            = models.IntegerField(default=0, verbose_name=u"喜欢数")

    class Meta:
        verbose_name = u"相亲信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.custom_description

class jobbole_detail_data(models.Model):
    detail_description_content = models.TextField(verbose_name=u"详细的自我描述")
    detail_info_url = models.URLField(max_length=300, verbose_name=u"详情链接")
    detail_info_url_object_id = models.CharField(max_length=50, verbose_name=u"链接的加密")

    class Meta:
        verbose_name = u"相亲详细信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.detail_description_content


class jobbole_image_data(models.Model):
    detail_info_url = models.URLField(max_length=300, verbose_name=u"详情链接")
    detail_info_url_object_id = models.CharField(max_length=50, verbose_name=u"链接的加密")
    image_url = models.CharField(max_length=300, verbose_name=u"妹子发的单张图片")

    class Meta:
        verbose_name = u"相亲图片信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.detail_info_url
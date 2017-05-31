# -*- encoding:utf-8 -*-
__author__ = 'Gh'
__date__ = '2017/5/25 下午4:39'

from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^$', views.index, name='index')
                ]
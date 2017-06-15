# -*- encoding:utf-8 -*-
from django.http import HttpResponse

import json
from .models import News, jobbole_date, jobbole_image_data, jobbole_detail_data
from gsite import settings
from django.views.generic.base import View
import leancloud
import logging

# Create your views here.
def index(request):
    NewsObject = News.objects.all()
    response_data = {}
    if NewsObject is None:
        response_data['result'] = 'error'
        response_data['success'] = False
        response_data['message'] = 'No datas'
    else:
        collect_datas = []
        for data in NewsObject:

            result_data = {}
            result_data['title']    = data.title
            result_data['summary']  = data.summary
            result_data['thumbnail']= settings.IMAGE_ROOT + data.thumbnail.url
            result_data['add_time'] = data.add_time.strftime("%Y-%m-%d %H:%M")

            # 发布者的相关信息
            pub_userInfo = {}
            pub_userInfo["nick_name"] = data.userinfo.nick_name
            pub_userInfo["avatar"]    = settings.IMAGE_ROOT + data.userinfo.avatar.url
            if pub_userInfo is not None:
                result_data["pub_userInfo"] = pub_userInfo

            if result_data is not None:
                collect_datas.append(result_data)

        response_data['result'] = collect_datas
        response_data['success'] = True
        response_data['message'] = 'success to get datas'

    return HttpResponse(json.dumps(response_data), content_type='application/json')

def job(request, page):
    # leancloud.init("xx", "xx")
    # logging.basicConfig(level=logging.DEBUG)
    # pageIndex = int(page)
    # if pageIndex * 50 > jobbole_date.objects.count() or pageIndex == 1 or pageIndex < 0:
    Jobs = jobbole_date.objects.all()[:50]
    # else:
    #     Jobs = jobbole_date.objects.all()[50*(pageIndex - 1):50 * pageIndex]
    # Jobs = jobbole_date.objects.all()

    results = {}
    datas = []
    for job in Jobs:

        # Jobbole_Date_Object = leancloud.Object.extend('Jobbole_Date_Object')
        # jobbole_object = Jobbole_Date_Object()
        #
        # jobbole_object.set('custom_description', job.custom_description)
        # jobbole_object.set('publish_time', job.publish_time)
        # jobbole_object.set('location', job.location)
        # jobbole_object.set('fav_num', job.fav_num)

        temp_dic = {}
        temp_dic['custom_description'] = job.custom_description
        temp_dic['publish_time']       = job.publish_time
        temp_dic['location']           = job.location
        temp_dic['fav_num']            = job.fav_num

        detail_info_url_object_id      = job.detail_info_url_object_id
        if detail_info_url_object_id:
            images = jobbole_image_data.objects.filter(detail_info_url_object_id=detail_info_url_object_id).values('image_url')
            temp_image_collection = []
            for image_object in images:
                temp_image_collection.append(image_object['image_url'])
            temp_dic['images'] = temp_image_collection
            # jobbole_object.set('images', temp_image_collection)

            detail_info = jobbole_detail_data.objects.filter(detail_info_url_object_id=detail_info_url_object_id).values('detail_description_content')
            temp_dic['detail_info'] = detail_info[0]['detail_description_content']
            # jobbole_object.set('detail_info', detail_info[0]['detail_description_content'])

        datas.append(temp_dic)
        # jobbole_object.save()

    results['list'] = datas
    results['result'] = "SUCCESS"

    return HttpResponse(json.dumps(results), content_type='application/json')
# -*- encoding:utf-8 -*-
from django.http import  HttpResponse

import json
from .models import News
from gsite import settings

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


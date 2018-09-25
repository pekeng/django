#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from .models import UserModel


def front_user_middleware(get_response):
    def middleware(request):
        # request到达view之前处理
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = UserModel.objects.get(id=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        reponse = get_response(request)
        # response到达浏览器之前代码
        return reponse

    return middleware


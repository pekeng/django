#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from .models import UserModel


def context_process(request):
    user_id = request.session.get('user_id')
    context = {}
    try:
        user = UserModel.objects.get(id=user_id)
        context['front_user'] = user
    except:
        pass
    return context

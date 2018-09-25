#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.shortcuts import redirect, reverse


def request_login_decorator(func):
    def wrapper(request, *args, **kwargs):
        user = request.front_user
        if user:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('login'))
    return wrapper

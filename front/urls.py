#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.urls import path, include
from .views import index, MyLoginView, MyLoginUp, my_logout, Transfer,my_index

urlpatterns = [
    path('index/', index, name='index'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('loginup/', MyLoginUp.as_view(), name='loginup'),
    path('logout/', my_logout, name='logout'),
    path('transfer/', Transfer.as_view(), name='transfer'),
    path('myindex/', my_index, name='myindex'),
]

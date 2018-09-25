#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from django import forms
from .models import UserModel


class LoginUpForms(forms.ModelForm):
    password_repeat = forms.CharField(max_length=11)

    def clean(self):
        cleaned_data = super(LoginUpForms, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError(message='2次密码输入的不一致')
        return cleaned_data

    class Meta:
        model = UserModel
        exclude = ['money']


class LoginForms(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['telephone', 'money']


class TransferForms(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'money']

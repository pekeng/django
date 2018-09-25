from django.db import models
from django.core import validators
from django.dispatch import receiver



class UserModel(models.Model):
    username = models.CharField(max_length=3)
    telephone = models.CharField(max_length=11,
                                 validators=[validators.RegexValidator(r'1[345678]\d{9}', message='请输入正确的手机格式')])
    password = models.CharField(max_length=11)
    money = models.FloatField(null=True)




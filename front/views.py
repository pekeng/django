from django.shortcuts import render, reverse, redirect
from django.views.generic import View
from front.froms import LoginUpForms, LoginForms, TransferForms
from .models import UserModel
from django.db.models import F
from django.http import HttpResponse
from .decorator import request_login_decorator
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


class MyLoginView(View):
    @staticmethod
    def get(request):
        return render(request, 'login.html')

    @staticmethod
    def post(request):
        forms = LoginForms(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = UserModel.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                print('账号或密码错误')
                request.session['user_id'] = None
                return redirect(reverse('login'))
        else:
            print(forms.errors)
            request.session['user_id'] = None
            return redirect(reverse('login'))


class MyLoginUp(View):
    @staticmethod
    def get(request):
        return render(request, 'loginup.html')

    @staticmethod
    def post(request):
        forms = LoginUpForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(reverse('login'))
        else:
            print(forms.errors)
            return redirect(reverse('loginup'))


@method_decorator(request_login_decorator, name='dispatch')
class Transfer(View):
    @staticmethod
    def get(request):
        return render(request, 'transfer.html', {})

    @staticmethod
    def post(request):
        forms = TransferForms(request.POST)
        if forms.is_valid():
            to_username = forms.cleaned_data.get('username')
            to_money = forms.cleaned_data.get('money')
            user = request.front_user
            if user and user.money >= to_money:
                UserModel.objects.filter(username=to_username).update(money=F('money') + to_money)
                user.money -= to_money
                user.save()
                return HttpResponse('转账成功')
            else:
                return HttpResponse('余额不足')
        else:
            print(forms.errors)
            return redirect(reverse('transfer'))


def my_logout(request):
    request.session.flush()
    return render(request, 'index.html')


def my_index(request):
    # user = User.objects.create_user('jianjian', email='9412490@qq.com', password='111111')
    # user.save()
    # user = User.objects.get(pk=1)
    # user.set_password('123')
    # user.save()
    username = 'jianjia'
    password = '123'
    user = authenticate(request, username=username, password=password)
    if user:
        print(user.is_active)
    else:
        print('验证失败')
    return HttpResponse('success')

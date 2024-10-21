from django.urls import resolve, reverse

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.base import kwarg_re


# Create your views here.
# def index(request):
#     # val = 'TTTT!'
#     # print(f'this is index html show... {val}')
#     # return render(request, 'index.html')
#     kwargs = {'year': '2019', 'month': '09', 'day': '17'}
#     args = ['2019', '09', '16']
#     # 使用reverse生成url
#     print(reverse('index:myvariable', args=args))
#     print(reverse('index:myvariable', kwargs=kwargs))
#     return HttpResponse(reverse('index:myvariable', args=args))

def myvariable(request, year, month, day):
    # args = ['2019', '09', '17']
    # result = resolve(reverse('index:myvariable', args=args))
    # print(f'kwargs {result.kwargs}')
    # print(f'url_name {result.url_name}')
    # print(f'namespace {result.namespace}')
    # print(f'app_name {result.app_name}')
    # print(f'view_name {result.view_name}')
    return HttpResponse(f'{year}年{month}月{day}日')

def index(request):
    print(reverse('index:turnTo'))
    return redirect(reverse('index:myvariable', args=['2019', '09', '17']))
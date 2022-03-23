from django.http import HttpResponse
from django.shortcuts import render

def runoob(request):
    context={}
    context['hello'] = 'Hello world!'
    context['name'] = '菜鸟教程'
    context['view_list'] = ['教程1', '教程2', '教程3']
    context['views_str'] = "<a href='https://www.runoob.com/'>点击跳转</a>"
    context['views_dict'] = {"name":"菜鸟教程", "level": "wonderful", "pages":18}
    return render(request, 'test/runoob.html', context)


def index(request):
    return render(request, 'layout.html')
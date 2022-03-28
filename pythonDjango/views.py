import imp
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from functools import wraps
from dataModel.models import User


def runoob(request):
    context={}
    context['hello'] = 'Hello world!'
    context['name'] = '菜鸟教程'
    context['view_list'] = ['教程1', '教程2', '教程3']
    context['views_str'] = "<a href='https://www.runoob.com/'>点击跳转</a>"
    context['views_dict'] = {"name":"菜鸟教程", "level": "wonderful", "pages":18}
    return render(request, 'test/runoob.html', context)



# 说明：这个装饰器的作用，就是在每个视图函数被调用时，都验证下有没法有登录，
# 如果有过登录，则可以执行新的视图函数，
# 否则没有登录则自动跳转到登录页面。
def check_login(f):
    @wraps(f)
    def inner(request,*arg,**kwargs):
        if request.session.get('is_login')=='1':
            return f(request,*arg,**kwargs)
        else:
            return HttpResponseRedirect('/login/')
            #return render(request,'account/login.html')
    return inner


@check_login
def index(request):
    # students=Students.objects.all()  ## 说明，objects.all()返回的是二维表，即一个列表，里面包含多个元组
    # return render(request,'index.html',{"students_list":students})
    # username1=request.session.get('username')
    user_id1=request.session.get('user_id')
    # 使用user_id去数据库中找到对应的user信息
    userobj=User.objects.filter(id=user_id1)
    print(userobj)
    if userobj:
        return render(request,'index.html',{"user":userobj[0]})
    else:
        return render(request,'index.html',{'user','匿名用户'})

def login(request):
    # 如果是POST请求，则说明是点击登录按扭 FORM表单跳转到此的，那么就要验证密码，并进行保存session
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username,password=password)   # 验证用户名和密码
        print(user)
        if user:
            #登录成功
            # 1，生成特殊字符串
            # 2，这个字符串当成key，此key在数据库的session表（在数据库存中一个表名是session的表）中对应一个value
            # 3，在响应中,用cookies保存这个key ,(即向浏览器写一个cookie,此cookies的值即是这个key特殊字符）
            request.session['is_login']='1'  # 这个session是用于后面访问每个页面（即调用每个视图函数时要用到，即判断是否已经登录，用此判断）
            request.session['username']=username  # 这个要存储的session是用于后面，每个页面上要显示出来，登录状态的用户名用。
            # 说明：如果需要在页面上显示出来的用户信息太多（有时还有积分，姓名，年龄等信息），所以我们可以只用session保存user_id
            request.session['user_id']=user[0].id
            return HttpResponseRedirect('/index/')
    # 如果是GET请求，就说明是用户刚开始登录，使用URL直接进入登录页面的
    return render(request,'account/login.html')


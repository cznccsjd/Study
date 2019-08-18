from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    # return HttpResponse("Hello Django!")
    return render(request, "index.html")

# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # if username == 'admin' and password == 'admin123':
        if user is not None:
            auth.login(request, user)       #登录
            # return HttpResponse('login success!')
            response = HttpResponseRedirect('/event_manage')
            # response.set_cookie('user', username, 3600)     #添加浏览器cookie
            request.session['user'] = username      #将Session信息记录到浏览器
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

def logout(request):
    return render(request, "index.html")

# 发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    # username = request.COOKIES.get('user', '')      #读取浏览器cookie
    username = request.session.get('user', '')      #读取浏览器session
    return render(request, 'event_manage.html', {"user":username, "events":event_list})

# 嘉宾管理
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.Get.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user":username, "guest":contacts})

# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user":username, "events":event_list})

if __name__ == '__main__':
    guest_manage()
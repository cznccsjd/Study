from django.shortcuts import render, get_object_or_404
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
    auth.logout(request)        #退出登录
    response = HttpResponseRedirect('/index')
    return response

# 发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    # username = request.COOKIES.get('user', '')      #读取浏览器cookie
    username = request.session.get('user', '')      #读取浏览器session
    return render(request, 'event_manage.html', {"user":username, "events":event_list})

# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 3)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user":username, "guests":contacts})
    # return render(request, "guest_manage.html", {"user":username, "guests":guest_list})

# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user":username, "events":event_list})

# 嘉宾名称搜索
@login_required
def search_guestName(request):
    username = request.sessoin.get('user','')
    search_name = request.GET.get('name','')
    guest_list = Guest.objects.filter(name__contains=search_name)
    return render(request, "guest_manage.html", {"user":username, "guests":guest_list})

# 签到页面
@login_required
def sign_index(request, eid):
    print("hello")
    event = get_object_or_404(Event, id=eid)
    # guests = Guest.objects.get(event_id=eid)
    guests = Guest.objects.all()
    guests_filter = Guest.objects.filter(sign=1)
    guest_num = len(guests)
    guest_signed = len(guests_filter)
    return render(request, 'sign_index.html', {'event':event, 'guest_num':guest_num, 'guest_signed':guest_signed})

# 签到动作
@login_required
def sign_index_action(request, eid):
    # get_object_or_404()默认调用Django的table.objects.get()方法，如果查询对象不存在，则会刨出一个Http404异常。这就省去了对table.objects.get()方法的异常断言
    event = get_object_or_404(Event, id=eid)
    guests = Guest.objects.all()
    guest_num = len(guests)
    guests_filter = Guest.objects.filter(sign=1)
    guest_signed = len(guests_filter)
    phone = request.POST.get('phone', '')
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event':event, 'guest_num':guest_num, 'guest_signed':guest_signed, 'hint':'phone error.'})

    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'event':event, 'guest_num':guest_num, 'guest_signed':guest_signed, 'hint':'event id or phone error.'})

    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign == 1:
        return render(request, 'sign_index.html', {'event':event, 'guest_num':guest_num, 'guest_signed':guest_signed, 'hint':'user has sign in.'})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        guest_signed += 1
        return render(request, 'sign_index.html', {'event':event, 'hint':'sign in success!', 'guest':result, 'guest_num':guest_num, 'guest_signed':guest_signed})

if __name__ == '__main__':
    # guest_manage()
    event_manage()
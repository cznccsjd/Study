#coding:utf-8
from django.http import JsonResponse
from sign.models import Event, Guest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
import time

# 添加发布会接口
def add_event(request):
    eid = request.POST.get('eid', '')                   #发布会id
    name = request.POST.get('name', '')                 #发布会标题
    limit = request.POST.get('limit', '')               #限制人数
    status = request.POST.get('status', '')             #状态
    address = request.POST.get('address', '')           #地址
    start_time = request.POST.get('start_time', '')     #发布会时间

    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status':10021, 'message':'Parameter error'})

    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022, 'message':'event id already exists'})

    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status':10023, 'message':'event name already exists'})

    if status != 1:
        status = 1

    try:
        Event.objects.create(id=eid, name=name, limit=limit, address=address, status=int(status), start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status':10024, 'message':error})

    return JsonResponse({'status':200, 'message':'add event success'})

# 添加嘉宾接口
def add_guest(request):
    realname = request.POST.get('realname', '')             #姓名
    phone = request.POST.get('phone', '')                   #手机号
    email = request.POST.get('email', '')                   #邮箱
    event_id = request.POST.get('eid', '')                  #关联发布会id

    if realname == '' or phone == '' or email == '' or event_id == '':
        return JsonResponse({'status':10021, 'message':'Parameter error'})

    result = Event.objects.filter(id=event_id)
    if not result:
       return JsonResponse({'status':10022, 'message':'event id is null'})

    result = Event.objects.get(id=event_id).status
    if not result:
        return JsonResponse({'status':10023, 'message':'event is not available'})

    result = Guest.objects.filter(phone=phone)
    if result:
        return JsonResponse({'status':10024, 'message':'phone is already exists'})

    result = Guest.objects.filter(email=email)
    if result:
        return JsonResponse({'status':10025, 'message':'email is already exists'})

    # 判断某个活动的嘉宾是否超过活动限制人数
    event_limit = Event.objects.get(id=event_id)
    guest_count = Guest.objects.get(event_id=event_id)
    if len(guest_count) >= event_limit:
        return JsonResponse({'status':10026, 'message':'event number is full'})

    # 判断某个嘉宾的注册时间是否超过活动开始时间
    event_time = Event.objects.get(id=event_id)     #发布会的时间
    etime = str(event_time).split(".")[0]
    timeArray = time.strptime(etime, "%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))

    now_time = str(time.time())     #当前的时间
    ntime = now_time.split(".")[0]
    n_time = int(now_time)

    if n_time >= e_time:
        return JsonResponse({'status':10027, 'message':'event has started'})

    try:
        Guest.objects.create(realname=realname, phone=int(phone), email=email, sign=0, create_time=n_time, event_id=int(event_id))
    except IntegrityError:
        return JsonResponse({'status':10028, 'message':'the event guest phone number repeat'})

    return JsonResponse({'status':200, 'message':'add guest success'})

# 发布会查询接口
def get_event_list(request):
    pass
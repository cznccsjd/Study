#coding:utf-8
from django.http import JsonResponse
from sign.models import Event, Guest
from django.core.exceptions import ValidationError

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

    result = Guest.objects.filter(id = event_id)
    if not result:
       return JsonResponse({'status':10022, 'message':'event id is null'})

    result = Guest.objects.filter(realname=realname)
    if result:
        return JsonResponse({'status':10023, 'message':'realname is already exists'})

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

    try:
        Guest.objects.create(realname=realname, phone=phone, email=email, sign=int(sign), create_time=create_time, event_id=event_id)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")


def home(request):
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        #if username == 'admin' and password == '123':
        if user is not None:
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)  设置浏览器cookie
            request.session['user'] = username
            return response
        else:
            return render(request,'login.html', {'error': 'username or password error!'})

#@login_required
def event_manage(request):
    # username = request.COOKIES.get('user') 获取Cookie值
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request, "event_manage.html",{"user": username,"events":event_list})

def guest_manage(request):
    # username = request.COOKIES.get('user') 获取Cookie值
    username = request.session.get('user', '')
    #guest_list = Guest.objects.get_queryset().order_by('id')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html",{"user": username,"guests":contacts})


def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username, "events": event_list})

def search_realname(request): #有分页BUG
    username = request.session.get('user', '')
    search_realname = request.GET.get("realname", "")
    guest_list = Guest.objects.filter(realname__contains=search_realname)
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request,"guest_manage.html",{"user": username,"guests":contacts})


def sign_index(request, eid):
    event = get_object_or_404(Event, id=eid)
    return render(request, 'sign_index.html', {'event': event})

def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone','')
    
    result = Guest.objects.filter(phone = phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event,'hint': 'phone error.'})
    
    result = Guest.objects.filter(phone=phone,event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'event': event,'hint': 'event id or phone error.'})
    
    result = Guest.objects.get(phone=phone,event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': "user has sign in."})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign = '1')
        return render(request, 'sign_index.html', {'event': event,'hint':'sign in success!','guest': result})
          

def logout(request):
    auth.logout(request) #退出登录
    response = HttpResponseRedirect('/login/')
    return response









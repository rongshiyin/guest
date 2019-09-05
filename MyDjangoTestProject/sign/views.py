from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
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

@login_required
def event_manage(request):
    # username = request.COOKIES.get('user') 获取Cookie值
    username = request.session.get('user')
    return render(request, "event_manage.html",{'user': username})
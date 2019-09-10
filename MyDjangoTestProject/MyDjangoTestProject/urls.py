"""MyDjangoTestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from sign import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('home/', views.home),
    path('login/', views.login),
    path('logout/', views.logout),
    path('login_action/', views.login_action),
    path('event_manage/', views.event_manage),
    path('guest_manage/', views.guest_manage),
    path('accounts/login/', views.login),
    path('search_name/', views.search_name),
    path('search_realname/', views.search_realname),
    re_path(r'^sign_index/(?P<eid>[0-9]+)/$', views.sign_index),
    re_path(r'^sign_index_action/(?P<eid>[0-9]+)/$', views.sign_index_action),
]

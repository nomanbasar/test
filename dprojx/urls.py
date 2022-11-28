from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from dappx import views

app_name = 'dappx' # Be careful setting the name to just /login use userlogin instead!

urlpatterns = [
 path('admin/', admin.site.urls),
 url(r'^$',views.index,name='index'),
 url(r'^special/',views.special,name='special'),
 url(r'^logout/$', views.user_logout, name='logout'),
 url(r'^register/$',views.register,name='register'),
 url(r'^user_login/$',views.user_login,name='user_login'),
]
from django.urls import path
from . import views
from django.contrib import admin

app_name ="dbinfo"

urlpatterns = [
    #path('templates/', views.index_template, name='index_template'),
    path('',views.top,name='top'),
    path('top/', views.top, name='top'),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout, name='logout'),
    #↑について、name='login'とすることで、{% app_name:login %}と指定したときにviewsのlogin関数を呼び出してくれます
]

from django.urls import path
from . import views
from django.contrib import admin

app_name ="dbinfo"

urlpatterns = [
    #path('templates/', views.index_template, name='index_template'),
    path('top/', views.top, name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]

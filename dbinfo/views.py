#from django.http.response import HttpResponse
#from .models import DBinfo

# def index_template(request):
#     products = DBinfo.objects.get(id=1)#id=1のレコードを抽出
#     myapp_data = {
#     'app': 'Django',
#     'is_weekday':True,
#     'name':products.name,#↑のレコードのname列の値を抽出
#     }
#     return render(request,'index.html', myapp_data)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.contrib.auth import logout

def signupuser(request):
    if request.method=='GET':
        return render(request, 'dbinfo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('/login')
            except IntegrityError:
                return render(request, 'dbinfo/signupuser.html',{'form': UserCreationForm(), 'error': 'Try again.'})
        else:#17
            return render(request, 'dbinfo/signupuser.html', {'form': UserCreationForm(), 'error': 'Password did not match.'})


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'dbinfo/login.html'


def Logout(request):
    """ログアウトページ"""
    logout(request)
    return render(request,'dbinfo/logout.html')

def top(request):
    return render(request, 'dbinfo/top.html')

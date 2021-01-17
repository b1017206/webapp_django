from django.shortcuts import render
from django.http.response import HttpResponse
from .models import DBinfo

def index_template(request):
    products = DBinfo.objects.get(id=1)#id=1のレコードを抽出
    myapp_data = {
    'app': 'Django',
    'is_weekday':True,
    'name':products.name,#↑のレコードのname列の値を抽出
    }
    return render(request,'index.html', myapp_data)

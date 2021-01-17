from django.shortcuts import render
from django.http.response import HttpResponse

def index_template(request):
    #products = DBinfo.objects.filter(id=1)
    myapp_data = {
    'app': 'Django',
    'is_weekday':True,
    #'id':products,
    }
    return render(request,'index.html', myapp_data)

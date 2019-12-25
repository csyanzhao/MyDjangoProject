from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Stu

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the myapp index. 喵")
    #return render(request, "index.html")

def stu(request):
    #获取所有stu表信息
    lists = Stu.objects.all()
    print(lists)
    #获取单条学生信息
    print(Stu.objects.get(id=1))

    return HttpResponse("ok")
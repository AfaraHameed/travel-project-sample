from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
# Create your views here.
def fun(request):
    obj = Place()
    obj.name = "kerala"
    obj.desc = "God's own country"
    obj.price = 1000
    return  render(request,'index.html' , {'result':obj})

def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1+num2
    return render(request,'result.html',{"result":result})
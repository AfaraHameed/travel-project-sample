from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Post
from django.db.models.functions import ExtractMonth, ExtractDay, ExtractYear


# Create your views here.
def first_load(request):
    obj = Place.objects.all()
    post = Post.objects.all()
    #month = post.date.strftime("%B")
    post = Post.objects.all().annotate(month=ExtractMonth('date'),day=ExtractDay('date'),year=ExtractYear('date'))
    return  render(request,'index.html' , {'results':obj,'post':post})

def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    result = num1+num2
    return render(request,'result.html',{"result":result})
from django.shortcuts import render,redirect
from django.http import HttpResponse
from foodsys.models import New_User,User_login
from . import forms
# Create your views here.
def home(request):
    my_dict = {'akash':"kumbhar"}
    return render(request,'index.html')
def login(request):
    form = forms.new_User()
    return render(request,'login.html',{'form':form})
def Menu(request):
    return render(request,'menu.html')
def order(request):
    user_list = New_User.objects.all()
    return render (request,'order.html',{'final_list':user_list})

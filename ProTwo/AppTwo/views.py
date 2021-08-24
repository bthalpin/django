from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    my_dict = {'title':'Index'}
    return render(request,'AppTwo/index.html',context=my_dict)

def help(request):
    my_dict = {'title':'Help Page'}
    return render(request,'AppTwo/index.html',context=my_dict)
def user(request):
    users = User.objects.order_by('last_name')
    data = {'user_info':users}
    return render(request,'AppTwo/userinfo.html',context=data)
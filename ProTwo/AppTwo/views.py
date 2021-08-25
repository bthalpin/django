from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUser

# Create your views here.
def index(request):
    my_dict = {'title':'Index'}
    return render(request,'AppTwo/index.html',context=my_dict)

def help(request):
    my_dict = {'title':'Help Page'}
    return render(request,'AppTwo/index.html',context=my_dict)
def users(request):
    users = User.objects.order_by('last_name')
    data = {'user_info':users}
    return render(request,'AppTwo/userinfo.html',context=data)
def user(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR')
    return render(request,'AppTwo/userinfo.html',context={'form':form})
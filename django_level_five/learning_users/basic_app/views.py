from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'basic_app/index.html',context=context_dict)

    
def other(request):
    dict = {'something':'somethingelse'}
    return render(request,'basic_app/other.html',context=dict)

    
def relative(request):
    dict = {'something':'somethingelse'}
    return render(request,'basic_app/relative_url_templates.html',context=dict)


from django.shortcuts import render

# Create your views here.
def index(request):
    #we can pass dictionary as context  to render
    context={
        'name':'Django',
        'version':'1.11'
    }
    return render(request,'index.html',context)
def info(request):
    return render(request,'my_info.html')
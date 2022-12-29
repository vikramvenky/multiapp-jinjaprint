from django.shortcuts import render

# Create your views here.

def jinja2(request):

    dict={'cap':'vikram','tap':'[+91 9989132102]'}
    return render(request,'second.html',dict)

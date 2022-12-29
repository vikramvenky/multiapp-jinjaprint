from django.shortcuts import render

# Create your views here.

def jinja(request):



    d={'name':'vikram','mobile':'[9989132102]'}
    return render(request,'first.html',d)
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from django.db import connection
# Create your views here.
def search(request):
    
    if request.method=="GET":
        st=request.GET.get('sname')
        if st!=None:
            fdata=front.objects.filter(name__icontains=st)
            cs=computerscience.objects.filter(name__icontains=st)
            ma=mechanicalautomobile.objects.filter(name__icontains=st)
            mp=mechanicalproduction.objects.filter(name__icontains=st)
            ee=electronics.objects.filter(name__icontains=st)
            mdata=magazines.objects.filter(name__icontains=st)
            
            
    return render(request,'user/search.html',{"f":fdata,"cs":cs,"ma":ma,"mp":mp,"ee":ee,"mag":mdata})
    


def home(request):
    fdata=front.objects.all().order_by('-id')[0:12]
    gdata=image.objects.all().order_by('-id')[0:6]

    return render(request,'user/index.html',{"f":fdata , "g":gdata})



def aboutus(request):

    return render(request,'user/aboutus.html')



def contactus(request):
    status=False
    if request.method=='POST':
        Name=request.POST.get("cname","")
        Mobile=request.POST.get("cnumber","")
        Email=request.POST.get("cemail","")
        Message=request.POST.get("cmsg","")
        res=contact(name=Name,number=Mobile,email=Email,message=Message)
        res.save()
        status=True
    return render(request,'user/contactus.html',{'S':status})


def cs(request):
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = computerscience.objects.all().filter(sem=x)
    else:
        pdata = computerscience.objects.all().order_by('-id')
    
    return render(request,'user/cs.html',{"cat":cdata,"books":pdata})


def ee(request):
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = electronics.objects.all().filter(sem=x)
    else:
        pdata = electronics.objects.all().order_by('-id')

    return render(request,'user/ee.html',{"cat":cdata,"books":pdata})


def gallery(request):

    return render(request,'user/gallery.html')


def ma(request):
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = mechanicalautomobile.objects.all().filter(sem=x)
    else:
        pdata = mechanicalautomobile.objects.all().order_by('-id')

    return render(request,'user/ma.html',{"cat":cdata,"books":pdata})


def mp(request):
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = mechanicalproduction.objects.all().filter(sem=x)
    else:
        pdata = mechanicalproduction.objects.all().order_by('-id')

    return render(request,'user/mp.html',{"cat":cdata,"books":pdata})


def mag(request):
    mdata=magazines.objects.all().order_by('-id')[0:]
    return render(request,'user/mag.html',{"maga":mdata})


#Notes Section start here....


def csnotes(request):
      
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = csnote.objects.all().filter(sem=x)
    else:
        pdata = csnote.objects.all().order_by('-id')

    return render(request,'user/csnotes.html',{"cat":cdata,"notes":pdata})

def manotes(request):
    
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = manote.objects.all().filter(sem=x)
    else:
        pdata = manote.objects.all().order_by('-id')

    return render(request,'user/manotes.html',{"cat":cdata,"notes":pdata})

def mpnotes(request):

    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = mpnote.objects.all().filter(sem=x)
    else:
        pdata = mpnote.objects.all().order_by('-id')

    return render(request,'user/mpnotes.html',{"cat":cdata,"notes":pdata})

def eenotes(request):
    
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = eenote.objects.all().filter(sem=x)
    else:
        pdata = eenote.objects.all().order_by('-id')

    return render(request,'user/eenotes.html',{"cat":cdata,"notes":pdata})


#question peper part start here.....


def cspaper(request):
    
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = csqp.objects.all().filter(sem=x)
    else:
        pdata = csqp.objects.all().order_by('-id')

    return render(request,'user/cspaper.html',{"cat":cdata,"paper":pdata})

def mapaper(request):
    
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = maqp.objects.all().filter(sem=x)
    else:
        pdata = maqp.objects.all().order_by('-id')

    return render(request,'user/mapaper.html',{"cat":cdata,"paper":pdata})

def mppaper(request):
    
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = mpqp.objects.all().filter(sem=x)
    else:
        pdata = mpqp.objects.all().order_by('-id')

    return render(request,'user/mppaper.html',{"cat":cdata,"paper":pdata})

def eepaper(request):
    cdata=category.objects.all().order_by()
    x=request.GET.get('abc')

    if x is not None:
        pdata = eeqp.objects.all().filter(sem=x)
    else:
        pdata = eeqp.objects.all().order_by('-id')

    return render(request,'user/eepaper.html',{"cat":cdata,"paper":pdata})



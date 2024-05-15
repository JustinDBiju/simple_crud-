from django.shortcuts import render , redirect
from .models import Member

def index(request):
    mem=Member.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    w=request.POST['first']
    x=request.POST['last']
    y=request.POST['email']
    z=request.POST['country']
    mem=Member(firstname=w,lastname=x,email=y,country=z)
    mem.save()
    return redirect('/')

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    w=request.POST['first']
    x=request.POST['last']
    y=request.POST['email']
    z=request.POST['country']
    mem=Member.objects.get(id=id)
    mem.firstname=w
    mem.lastname=x
    mem.email=y
    mem.country=z
    mem.save()
    return redirect("/")
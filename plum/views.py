from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import user
from .models import *
from django.http import JsonResponse



from django.contrib.auth import authenticate,login,logout

def form(request):
    if request.method=="POST":
       name=request.POST['name']
       contact=request.POST['contact']
       email=request.POST['email']
       password=request.POST['password']
       reg= stform(name=name,contact=contact,email=email,password=password)
            
       reg.save()
    
       return HttpResponseRedirect("/login/")
    else:
        fr=user()
    return render(request,"signup.html",{'form':fr})
def index(request):
    return render(request,'index.html')
    '''try:
        email=request.session['pro']
        if email==None:
            return HttpResponseRedirect("/login/")
        return render(request,'index.html')
    except:
        return HttpResponseRedirect("/login/")'''
def elements(request):
    return render(request,"elements.html")
def home(request):
    return render (request,"home.html")
def login(request):
    try:
        if request.method=="POST":
            username=request.POST['uname']
            print(username)
            password=request.POST['psw']
            user=stform.objects.filter(name=username,password=password)
            k=user[0]
            request.session["pro"]=k.email
            if k is not None:
                return HttpResponseRedirect("/index/")                  
        else:
            return render(request,"login.html")
    except:
        return HttpResponseRedirect("/login/")
def taps(request):
    product1=products.objects.filter(category=1)
    if request.method=="POST":
        pro=request.POST['pid']
        qty=request.POST['qty']
        cp=products.objects.filter(id=pro)
        
        
          
       
    
        return render(request,"cart.html",{'cp':cp,'qty':qty})
    else:
        pass

        
   
    
    return render(request,"taps.html",{'k':product1})
def pipes(request):
    pro =products.objects.filter(category=3)
    
    
        
    return render(request,"pipes.html",{'k':pro})
def shower(request):
    # if product1=products.objects.all():
    #    cat=category.objects.get(id=2)  
    pro=products.objects.filter(category_id=2);
    return render(request,"shower.html",{'k':pro})

def logout(request):
    del request.session['pro']
    return HttpResponseRedirect("/login/")



# Create your views here.
def cart(request):
    
    
    
    return render(request,"taps.html")
  
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode , urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .models import Product,Order
import json

# Create your views here.
# Create your views here.
def index(request):  
    products = Product.objects.all() 
    return render(request,"index.html",{'products':products})

def signup(request):
    if request.method == "POST":
        
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username = username ):
            messages.error(request,"Username already exist! please try anothrt one")
            return redirect('index')
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already exist! please try anothrt one")
            return redirect('index')
        
        if len(username) >10 :
            messages.error(request,"Username must be under 10 charecters")
            #return redirect('home')

        if pass1 != pass2 :
            messages.error(request,"password is not match !")
        
        if not username.isalnum():
            messages.error(request,"Username must be Alpha-Numaric")
            return redirect('index')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        #myuser.is_active = False
        myuser.is_active = True
        myuser.save()

        messages.success(request,"your account has been successfully created. wer have send you a cnformation email please confirm your email ")

        return redirect("signin")

    return render(request,"signup.html")

def signin(request):   
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)
    
        if user is not None:
            login(request,user)
            fname = user.first_name
            
            products = Product.objects.all()
            return  redirect('index')# render(request, "index.html",{'fname':fname,'products':products})

        else :
            messages.error(request,"Bad Credentials!")
            return redirect('index')

    return render(request,"login.html")

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully!")
    return redirect('index')

def checkout(request):  
    if request.method=="POST":         
        user = request.user.username
        items_json = request.POST.get('itemJson','')
        
        mylist = []
        items_json1 = json.loads(items_json)
        print(items_json)
        for item in items_json1:
            mylist.append(items_json1[item])
        mylist = json.dumps(mylist)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + " " + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip','')
        phone = request.POST.get('phone','')
        grand_total = request.POST.get('grand_total','')
        order = Order(items_json=mylist,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,user=user,grand_total=grand_total)
        order.save()
        thank = True
        return render(request,'checkout.html',{'thank':thank})

    return render(request,"checkout.html",{})

def history(request):
    user = request.user.username
    orders = Order.objects.filter(user=user) 
    for order in orders:
        order.items_json = json.loads(order.items_json)
        
    return render(request,"history.html",{'orders':orders})



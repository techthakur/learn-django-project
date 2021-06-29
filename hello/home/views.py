from django.http.response import HttpResponse
from home.models import Contact
from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.models import User




# Create your views here.

def home(request):
    return render(request,  "home.html")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        if len(name)<2  or len(email)<2 or len(phone)<10  or len(desc)<4:
            messages.error(request, ' Plese fill form corretly ')          # here is error is not working i dnot know why 
        else:
            contact= Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, 'Yur Message has been sent!')

    return render(request,  "contact.html")
 


def search(request):
    allPosts = Post.objects.all()
    params = {'allPosts': allPosts}
    return render(request, "search.html"  , params)







def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname =request.POST['fname']
        lname =request.POST['lname']
        email= request.POST['email']
        pass1 =request.POST['pass1']
        pass2 =request.POST['pass2']


        # cheack valied form or not 
        if len (username) >10 :
            messages.error(request, "please take user name under 10 chareters ")
            return redirect('home')

        
        if not username.isalnum():
            messages.error(request, " take user name must be only letter oe number  ")
            return redirect('home')
        



        # this is me cheack 
        if len (fname) >10 :
            messages.error(request, "please fill first name corretly  ")
            return redirect('home')
        

        

        if len (lname) >10 :
            messages.error(request, " please fill last name correly ")
            return redirect('home')



        if pass1 != pass2:

            messages.error(request, "password dose not match please match your password  ")
            return redirect('home')






        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " your acount has been created successfully ")
        return redirect('home') 
    
    
    else:

        return HttpResponse("  error  ")













def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username = loginusername, password = loginpass)
        

        if user is not None:
            login(request,user)
            messages.success(request, 'seccussfully logdin ')
            return redirect('home')
        
        else:
            messages.success(request, ' invilade , please try again ')
            return redirect('home')







    return HttpResponse("  404-   not found  ")









def handleLogout(request):
    logout(request)
    messages.success(request,' successfully logout ')
    return redirect('home')


    #return HttpResponse(" logout ")






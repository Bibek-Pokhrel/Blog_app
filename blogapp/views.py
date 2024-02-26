import datetime

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from . models import User_register
from .models import BlogTable
from .models import commenttable



# Create your views here.

def base(request):
    return render(request,'blogapp/base.html')


@login_required(login_url='/')
def home(request):
    if request.method=="POST":
        title=request.POST['title']
        description=request.POST['description']
        image=request.POST['image']
        username=request.user.username
        
        user=User.objects.first()
        
        BlogTable.objects.create(title=title,description=description,image=image,
                                 created_by=user,created_at=datetime.datetime.now(),username=username)
        
    data=BlogTable.objects.all()
    data1=commenttable.objects.filter(is_delete=False)
    
    
    
        
    return render(request,'blogapp/home.html',{'data':data,'data1':data1})
 
 
def blogcomment(request,pk):
    
    if request.method=="POST":
        blogcomment=request.POST['blogcomment']
        username=request.user.username
        
        commenttable.objects.create(comment_id=pk,comment_time=datetime.datetime.now(),
                                    comment_by=username,cmt=blogcomment)
        
    data=BlogTable.objects.all()
    data1=commenttable.objects.filter(is_delete=False)
    return render(request,'blogapp/home.html',{'data':data,'data1':data1})
       

def cmtdelete(request,pk):
    cmt=commenttable.objects.get(id=pk)
    cmt.is_delete=True
    cmt.save()
    return redirect("/home")


def cmtedit(request,pk):
    cmt1=commenttable.objects.get(id=pk)
    
    if request.method == "POST":
        cmt=request.POST['blogcomment']
        commenttable.objects.filter(id=pk).update(cmt=cmt)
        return redirect("/home")
    
    return render(request,'blogapp/editcmt.html',{'cmt1':cmt1})

def userlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        # username1=User_register.objects.filter(username=username)
        # if not username1:
        #     err={"invalid username and password":""}
        #     return render(request,'blogapp/login.html',{'err':err})
            
        # for data in username1:
        #     username2=data.username
        #     password2=data.password
            
        #     if username2 == username and password2==password:
        #         return redirect("/home")
            
        #     else:
        #         err={"invalid username and password":""}
        #         return render(request,'blogapp/login.html',{'err':err})
        
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("/home")
        else:
            logout(request)
            err={"invalid username and password":""}
            return render(request,'blogapp/login.html',{'err':err})
        
        
    return render(request,'blogapp/login.html')

def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        gender=request.POST['gender']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password != confirmpassword:
            pas={"error ! enter same password":""}
            return render(request,'blogapp/register.html',{'pas':pas})
        
        User_register.objects.create(firstname=firstname,lastname=lastname,gender=gender,
                                     email=email,username=username,password=password)
        User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        
        
    return render(request,'blogapp/register.html')



def user_logout(request):
    logout(request)
    
    return redirect("/")




def profile(request):
    data=BlogTable.objects.filter(username=request.user.username)
    
    data1=commenttable.objects.filter(is_delete=False)
    return render(request,'blogapp/profile.html',{'data':data,'data1':data1})
       

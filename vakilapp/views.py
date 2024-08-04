from django.shortcuts import render,redirect,HttpResponse
from vakilapp.models import *
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    team=Team_Member.objects.all()
    context={'team':team}
    return render(request,"index.html",context)

def send_msg(request):

    if request.method == "POST":
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Subject= request.POST.get('subject')
        Message=request.POST.get('message')

        user=customer(Name=Name,Email=Email, Phone= Phone,Subject=Subject,Message=Message,Date=datetime.today())
        user.save()

    return redirect('index')


#----------------------------------------Admin:-Login--------------------------------------------------
def admin_login (request):

        if request.method == "POST":
            u_name = request.POST.get('username')
            password = request.POST.get('Password')

            if not User.objects.filter(username=u_name).exists():
                messages.error(request,'Invalid Username')
                return redirect('admin_login')

            user=authenticate(username=u_name,password=password)

            if user is None:
                messages.error(request,'Invalid Password')
                return redirect('admin_login')
            else:
                 login(request,user)
                 return redirect('admin_home')
            
        return render(request,"admin_login.html")


#----------------------------------------Admin:-LogOut--------------------------------------------------
def logout_admin (request):
           
        logout(request)
        return redirect('admin_login')

#----------------------------------------Admin:-register--------------------------------------------------
def admin_register (request):
        
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            u_name = request.POST.get('username')
            password = request.POST.get('password')

            user=User.objects.filter(username=u_name)

            if not has_alpha_num_sym(password):
                messages.error(request,'Password not alphanumric and Symbolic')
                return redirect('admin_register')
            
            elif len(password)<8:
                messages.error(request,'Password Must be min 8 char length')
                return redirect('admin_register')
            
            if user:
                messages.error(request,'Username is already taken')
                return redirect('admin_register')

            
            user=User.objects.create_user(first_name=fname,last_name=lname,username=u_name)
            user.set_password(password)
            user.save()
            messages.info(request,'Account Created Successfully!!')
            return redirect('admin_register')
        
        return render(request,"admin_register.html")


#for checking given str is sym or not
def has_alpha_num_sym(input_string):
    has_alpha = False
    has_num = False
    has_sym=False

    for char in input_string:
        if char.isalpha():
            has_alpha = True
        elif char.isdigit():
            has_num = True
        if not char.isalnum():
            has_sym=True

    return has_alpha and has_num and has_sym
#----------------------------------------Admin:-Home--------------------------------------------------
@login_required(login_url='admin_login')
def admin_home (request):

    # current_time = datetime.now().time()
    
    # greet=greet_fun()
    day_count=customer.objects.filter(Date=datetime.today()).count()
    total_count=customer.objects.count()

    context={'day_count':day_count,'total_count':total_count,}
    return render(request,"admin_home.html",context)


# def greet_fun():
#     current_time = datetime.now().time()
    
#     if current_time < datetime.time(12, 0):
#         print("Good Morning!")
#     elif current_time < datetime.time(17, 0):
#         print("Good Afternoon!")
#     else:
#         print("Good Evening!")
#----------------------------------------Admin:-alert--------------------------------------------------
@login_required(login_url='admin_login')
def admin_alert (request):
    return render(request,"admin_alert.html")

#----------------------------------------Admin:-team--------------------------------------------------
@login_required(login_url='admin_login')
def admin_team(request):

    member=Team_Member.objects.all()
    result=None
    data=None
    
    if request.GET.get('Search'):
        member= member.filter(Name__icontains=request.GET.get('Search'))
        data=request.GET.get('Search')[0:7]
        result=True
        
    if not member:
         data=request.GET.get('Search')[0:7]
         result=False
  
    context={'member':member,'result':result,"data":data}
    return render(request,"admin_team.html",context)

#----------------------------------------Admin:-team--------------------------------------------------
@login_required(login_url='admin_login')
def add_team(request):
     
    if request.method == "POST":
        
        name = request.POST.get('Name')
        Qulification= request.POST.get('Qulification')
        Description = request.POST.get('Description')
        photo=request.FILES.get('Photo')

        add_team=Team_Member(Name=name,Qualification=Qulification, Description=Description,Image=photo)
        add_team.save()

        return redirect('admin_team')
    
#----------------------------------------Admin:-update team--------------------------------------------------    
@login_required(login_url='admin_login')
def update_team(request,id):
     
    got_id=Team_Member.objects.get(id=id)


    if request.method == "POST":
        
        name = request.POST.get('Name')
        Qulification= request.POST.get('Qulification')
        Description = request.POST.get('Description')
        photo=request.FILES.get('Photo')

        got_id.Name=name
        got_id.Qualification=Qulification
        got_id.Description=Description
    
        if photo:
            got_id.Image=photo

        got_id.save()
        return redirect('/admin_team')
    
    context={'qurryset':got_id}
    
    return render(request, "admin_update.html",context)
    

#----------------------------------------Admin:-delete team--------------------------------------------------
@login_required(login_url='admin_login')
def delete_team(request):
     
    id=request.GET['id']
    Team_Member.objects.filter(id=id).delete()
    return redirect('/admin_team')


#----------------------------------------Admin:-Messages--------------------------------------------------
@login_required(login_url='admin_login')
def admin_msg(request):

    customer_messages=customer.objects.all().order_by('-id')
    result=None
    data=None
    
    if request.GET.get('Search'):
        customer_messages= customer_messages.filter(Name__icontains=request.GET.get('Search'))
        data=request.GET.get('Search')[0:7]
        result=True
        
    if not customer_messages:
         data=request.GET.get('Search')[0:7]
         result=False

    context={'customer_messages':customer_messages,'result':result,"data":data}
    return render(request,"admin_msg.html",context)


#----------------------------------------Admin:-Delete Messages--------------------------------------------------
@login_required(login_url='admin_login')
def delete_msg(request):
     
    id=request.GET['id']
    customer.objects.filter(id=id).delete()
    return redirect('/admin_msg')


@login_required(login_url='admin_login')
def admin_update(request):
    return render(request,"admin_update.html")
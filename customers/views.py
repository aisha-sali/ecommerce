from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from  . models import Customer
from django.contrib import messages
# Create your views here.
def show_account(request):
        if request.POST and 'register' in request.POST :
             try:
                    
                    username=request.POST.get('username')
                    password=request.POST.get('password')
                    email=request.POST.get('email')
                    address=request.POST.get('address')
                    phone=request.POST.get('phone')
                #create user accounts 
                    user=User.objects.create(
                        username=username,
                        password=password,
                        email=email
                    )
                    #create customer account
                    customer=Customer.objects.create(
                        user=user,
                        phone=phone,
                        address=address
                    )
                    return redirect('home')
             except Exception as e:
                
                 error_message="Duplicate Usrname"
                 messages.error(request,error_message)
        return render(request,'account.html')
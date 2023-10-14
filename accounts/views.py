
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from cmath import log

from products.models import Coupon, Product, SizeVariant
from .models import Cart, CartItems, Profile

# Create your views here.

def Login_page(request):
    if request.method=='POST':
        email=request.POST.get('username')
        password=request.POST.get('password')
        
        user_obj=User.objects.filter(username=email)
        
        if not user_obj.exists():
            messages.warning(request,'Account not found')
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].profile.is_email_varified:
            messages.warning(request,'Your account is not varified')
            return HttpResponseRedirect(request.path_info)
            
        
        user_obj=authenticate(username=email,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        
        messages.warning(request,'Invalid credentails')
        return HttpResponseRedirect(request.path_info) 
    return render (request,'accounts/login.html')

# ----------------------------  SignUp Functon ------------------------------------------------

def SignUp_page(request):
    if request.method=='POST':
        
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user_obj=User.objects.filter(username=email)
        
        if user_obj.exists():
            messages.success(request,'email is taken')
            return HttpResponseRedirect(request.path_info)
        
        user=User.objects.create(first_name=firstname,last_name=lastname,email=email,username=email,password=password)
        user.set_password(password)
        user.save()
        
        messages.warning(request,'email has been sent to your mailbox')
        return HttpResponseRedirect(request.path_info)
    
    return render (request,'accounts/register.html')



def activate_email(request,email_token):
    try:
        user=Profile.objects.get(email_token=email_token)
        user.is_email_varified=True
        user.save()
        return redirect('/')
    except Exception as e:
        return  HttpResponse(" invalid email Token ") 




# def Add_to_Cart(request,uid):
    
#     variant=request.GET.get('variant') 
#     product=Product.objects.get(uid=uid)
#     user=request.user 
    
#     cart, _=Cart.objects.get_or_create(user=user, is_paid=False)  
      
#     cart_item = CartItems.objects.create(cart=cart, product=product)
    
#     if variant:
#         variant=request.GET.get('variant')
#         size_variant=SizeVariant.objects.get(size_name=variant)
#         cart_item.size_variant=size_variant
#         cart_item.save()
        
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def remove_cart(request,cart_item_uid):
    try:
        cart_item=CartItems.objects.get(uid=cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



         
def cart(request):
    cart_obj= Cart.objects.get(is_paid=False,user=request.user)
    if request.method=="POST":
        coupon=request.POST.get('coupon')
        coupon_obj=Coupon.objects.filter(coupon_code__icontains = coupon)
        if not coupon_obj.exists():
            messages.warning(request,'Invalid Coupon')
                        
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if cart_obj.exists():
             messages.warning(request,'Coupon Already exists')
                        
             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        cart_obj.coupon=coupon_obj
        cart_obj.save()
        messages.success(request,'Coupon Applied')
                        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
               
    context={'cart':cart_obj}    
    return render (request,'accounts/cart.html',context)        
      

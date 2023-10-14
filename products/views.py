from django.shortcuts import  render
from .models import Product, SizeVariant
from accounts.models import Cart, CartItems
from django.http import HttpResponseRedirect


from products.models import Product

def get_products(request,slug): 
    print('*******')
    print(request.user)
    print('*****')
    print(request.user.profile.get_cart_count)
     
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product}
        if request.GET.get('size'):
            
            size = request.GET.get('size')     
            price = product.get_product_price_by_size(size)
            
            context['selected_size'] = size
            context['updated_price'] = price
            
            print(price)
        return render(request, 'product/products.html', context=context)  
    except Exception as e:
        print(e)


def Add_to_Cart(request,uid):
    variant=request.GET.get('variant')
        
    product=Product.objects.get(uid=uid)
    user=request.user 
    cart,_=Cart.objects.get_or_create(user=user, is_paid=False)
    cart_item=CartItems.objects.create(cart=cart,product=product)
    if variant:
        variant=request.GET.get('variant')
        size_variant=SizeVariant.objects.get(size_name=variant)
        cart_item.size_variant=size_variant
        cart_item.save()
    return HttpResponseRedirect(request.path_info)   
    



    
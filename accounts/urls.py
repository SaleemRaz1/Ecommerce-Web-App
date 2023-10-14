from django.urls import path
from accounts.views import Login_page, SignUp_page, activate_email, cart, remove_cart
from products.views import Add_to_Cart




urlpatterns = [
    path('login/',Login_page,name="login"),
    path('register/',SignUp_page,name="signup"),
    path('activate/<email_token>',activate_email,name="activate_email"),
    path('cart/',cart,name="cart"),
    path('add-to-cart/<uid>/',Add_to_Cart,name="add_to_cart"),
    
    path('remove_cart/<cart_item_uid>/',remove_cart,name="remove_cart"),
    
]

from django.urls import path
from .import views
# from products.views import get_products

urlpatterns = [
    path('<slug>/',views.get_products,name="get_product"),
 
    

    
]

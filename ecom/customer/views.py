from django.shortcuts import render,redirect
from common.models import Customer
from customer.models import Cart
from reseller.models import Product

# Create your views here.
def customer_home (request):
    products=Product.objects.all()
    return render (request,'customerapp/customer_home.html',{"product":products})

def add_cart (request,pid):
    product=Product.objects.get(id=pid)
    user=Customer.objects.get(id=request.session['customer_id'])
    cart_exist=Cart.objects.filter(product=pid,user=request.session['customer_id']).exists()
    if not cart_exist:

        cart=Cart(product=product,user=user)
        cart.save()
    return redirect('customer_home')

def view_cart (request):
    cart_product=Cart.objects.filter(user=request.session['customer_id'])
    return render (request,'customerapp/view_cart.html',{"cart_product":cart_product})
    
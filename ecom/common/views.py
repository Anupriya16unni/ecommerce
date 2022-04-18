from django.shortcuts import render

# Create your views here.
def common_home (request):
    return render (request,'commonapp/common_home.html')

def customer_login (request):
    return render (request,'commonapp/customer_login.html')

def reseller_login (request):
    return render (request,'commonapp/reseller_login.html')

def reseller_signup (request):
    return render (request,'commonapp/reseller_signup.html')

def customer_signup (request):
    return render (request,'commonapp/customer_signup.html')

def add_product (request):
    return render (request,'commonapp/add_product.html')

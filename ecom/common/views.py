import email
from email.headerregistry import Address
from django.shortcuts import render
from .models import Customer, Reseller

# Create your views here.
def common_home (request):
    username="anu"
    type="customer"
    return render (request,'commonapp/common_home.html',{"user":username,"type":type})

def customer_login (request):
    return render (request,'commonapp/customer_login.html')

def reseller_login (request):
    return render (request,'commonapp/reseller_login.html')

def reseller_signup (request):
    if request.method=='POST':
        res_name=request.POST['name']
        res_email=request.POST['email']
        res_address=request.POST['address']
        res_mobile_number=request.POST['phn']
        res_adhar_number=request.POST['adhar']
        res_holder_name=request.POST['holder']
        res_account_number=request.POST['acc_num']
        res_ifsc_code=request.POST['ifsc']
        res_username=request.POST['uname']
        res_password=request.POST['pass']

        res_obj=Reseller(name=res_name,email=res_email,address=res_address,mobile_number=res_mobile_number,adhar_number=res_adhar_number,holder_name=res_holder_name,account_number=res_account_number,ifsc_code=res_ifsc_code,user_name=res_username,password=res_password)
        res_obj.save()
    return render (request,'commonapp/reseller_signup.html')

def customer_signup (request):
    if request.method=="POST":
        cust_name=request.POST["name"]
        cust_address=request.POST["address"]
        cust_email=request.POST['email']
        cust_mobile_number=request.POST['phn']
        cust_username=request.POST['uname']
        cust_password=request.POST['pass']

        obj=Customer(name=cust_name,address=cust_address,email=cust_email,mobile_number=cust_mobile_number,user_name=cust_username,password=cust_password)
        obj.save()
    return render (request,'commonapp/customer_signup.html')

def add_product (request):
    return render (request,'commonapp/add_product.html')

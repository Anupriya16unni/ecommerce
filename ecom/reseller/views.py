from django.shortcuts import render
from common.models import Reseller
from reseller.models import Product

# Create your views here.
def add_product (request):
    if request.method=='POST':
        p_name=request.POST['p_name']
        p_desc=request.POST['p_desc']
        p_price=request.POST['p_price']
        p_stock=request.POST['p_stock'] 
        p_img=request.FILES['p_img']

        data=Reseller.objects.get(id=request.session['seller_id'])
        prod=Product(product_name=p_name,desc=p_desc,stock=p_stock,image=p_img,price=p_price,seller_id=data.id)
        prod.save()
    return render (request,'resellerapp/add_product.html')

def reseller_home (request):
    return render (request,'resellerapp/reseller_home.html')
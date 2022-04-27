from django.urls import path
from .import views

urlpatterns=[
    path('add_product',views.add_product,name="add_product"),
    path('reseller_home',views.reseller_home,name="reseller_home")
]
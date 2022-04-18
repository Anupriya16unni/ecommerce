from operator import irshift
from django.urls import path
from .import views
urlpatterns=[
   path('common_home',views.common_home,name="common_home"),
   path('reseller_login',views.reseller_login,name="reseller_login"),
   path('reseller_signup',views.reseller_signup,name="reseller_signup"),
   path('customer_signup',views.customer_signup,name="customer_signup"),
   path('customer_login',views.customer_login,name="customer_login"),
   path('add_product',views.add_product,name="add_product")  
]
from django.urls import path
from .import views
urlpatterns=[
    path('customer_home',views.customer_home,name="customer_home"),
    path('cart/<int:pid>',views.add_cart,name="addToCart"),
    path('cart',views.view_cart,name="view_cart")
]
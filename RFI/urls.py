from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('products/',views.product,name="products"),
    path('Customer/<str:pk>',views.customer,name='Customer'),
    path('Create_order',views.createOrder,name='Create_order'),
    path('update_order/<str:pk>',views.updateOrder,name='update_order'),
    path('delete_order/<str:pk>',views.deleteOrder,name='delete_order'),
]

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Order,Customer,Product
from .forms import *

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    print(orders.filter(status='Delivered'))
    total_customers = customers.count()

    total_orders = orders.count()
    print(total_orders)
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()
    print(delivered)
    print(pending)

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}
    print(orders)

    return render(request,'RFI/dashbord.html',context)

def product(request):
    product=Product.objects.all()
    return render(request, 'RFI/product.html',{'product':product})

def customer(request, pk):
    customer=Customer.objects.get(id=pk)

    #query customer child object it should small letter ex:order_set
    order=customer.order_set.all()
    order_count=order.count()
    context={'customer':customer,'order':order,'order_count':order_count}
    return render(request, 'RFI/Customer.html',context)

# Create your views here.
def createOrder(request):

    form=OrderForm()
    if request.method=='POST':
        print("requesting method is post")
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            #back to home
            return redirect('/')

    context={'form':form}
    return render(request,'RFI/order_form.html',context)

def updateOrder(request,pk):
    #auto populate or prefilled form
    order=Order.objects.get(id=pk)
    #pass order value to form
    form = OrderForm(instance=order)
    if request.method=='POST':
        print("requesting method is post")
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            #after update save the value
            form.save()
            #back to home
            return redirect('/')
    context={'form':form,'order':order}
    return render(request,'RFI/order_form.html',context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    #{'template based name';passing val} template based name- presenet in html
    context={'item':order}
    return render(request, 'RFI/delete_order.html', context)

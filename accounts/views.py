from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import *
from django.urls import reverse_lazy
from django.views.generic.edit import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()


    return render(request,"accounts/dashboard.html",{"orders":orders,"customers":customers,"total_customers":total_customers,"total_orders":total_orders,"delivered":delivered,"pending":pending})

def products(request):
    products = Product.objects.all()
    return render(request,"accounts/products.html",{"products": products})

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    orders_count = orders.count()
    context = {
        "customer" : customer,
        "orders" : orders,
        "orders_count": orders_count,
    }
    return render(request,"accounts/customer.html",context)



def update_order(request,pk):
    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "accounts/order_form.html", {"products": products, "form": form})


class UpdateOrder(UpdateView):
    model = Order
    fields = '__all__'
    template_name = "accounts/order_form.html"
    success_url = reverse_lazy("home")

class DeleteOrder(DeleteView):
    model = Order
    success_url = reverse_lazy("home")

class CreateOrder(CreateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy("home")
    template_name = "accounts/order_create_form.html"

class CreateCustomer(CreateView):
    model = Customer
    fields = "__all__"
    success_url = reverse_lazy("home")
    template_name = "accounts/customer_create_form.html"
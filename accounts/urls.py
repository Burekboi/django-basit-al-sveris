from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("customer/<int:pk>/", views.customer, name="customer"),

    path("updateform/<int:pk>/", views.UpdateOrder.as_view() , name="update"),
    path("deleteform/<int:pk>/", views.DeleteOrder.as_view() , name="delete"),
    path("create_order/", views.CreateOrder.as_view() , name="create"),
    path("create_customer/", views.CreateCustomer.as_view() , name="create_customer"),

]


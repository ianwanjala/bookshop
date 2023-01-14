from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer,Address,Books
from django.template import loader


# Create your views here.

def index(request):
    """view for home page function"""
    customer_list = get_object_or_404(Customer)
    context ={'customer':Customer}
    return HttpResponse(render(request,'index.html',context))

def address(request):
    address_list=get_object_or_404(Address)
    context={'address':address}
    return HttpResponse(render(request,'list.html',context))

def books(request):
    book_list=get_object_or_404(Books)
    context={'books':books}
    return HttpResponse(render(request,'list.html',context))


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Customer,Address,Books
from django.template import loader


# Create your views here.

def index(request):
    """view for home page function"""
    #customer_list = get_object_or_404(Customer)
    index_list = Customer.objects.all()
    address_list=Address.objects.all()
    book_list=Books.objects.all()
    #customer = Customer.objects.get(pk=customer_id)
    #context ={'customer':customer_list}
    return HttpResponse(render(request,'index.html',{'index_list':index_list,'address_list':address_list,'book_list':book_list}))

def address(request):
    address_list= Address.objects.all()
    #context={'address':address}
    return HttpResponse(render(request,'address_list.html',{'address_list':address_list}))

def books(request):
    book_list=Books.objects.all()
    context={'books':books}
    return HttpResponse(render(request,'book_list.html',{'book_list':book_list}))


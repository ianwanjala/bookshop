from django.urls import path
from . import views

urlpatterns = [ 
            path('', views.index, name='index'),
            path('',views.customer, name = 'customer'),
            path ('',views.address, name ='customer'),
            path('',views.book, name = 'books'),
            ]

from django.urls import path
from . import index

urlpatterns = [ 
            path('', index.index, name='index'),
            path ('',index.address, name ='address'),
            path('',index.books, name = 'books'),
            ]

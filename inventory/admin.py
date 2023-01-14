from django.contrib import admin
from .models import customer,address,books


# Register your models here.

admin.site.register(customer)
admin.site.register(address)
admin.site.register(books)

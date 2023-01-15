from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50, null=True, help_text ='Enter your first name')
    email = models.EmailField(unique = True, null = True )
    phone = models.CharField(max_length=20, null = True)


    def __str__(self):
        return self.name #+ " " + self.phone

class Address(models.Model):
#    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null = True)
 #   zip_code = models.CharField(max_length=20,  null = True   )
#    town = models.CharField(max_length=255,null = True)
    town = models.CharField(max_length=70, help_text='Enter your Town',null = True)

    def __str__(self):
        return self.town # street_address #+ ", " + self.city 

class Books(models.Model):
    title = models.CharField(max_length=255,null = True)
    author = models.CharField(max_length=255,null = True)
    ISBN = models.CharField(max_length=255,null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null = True)

    def __str__(self):
        return self.title #+ " by " + self.author

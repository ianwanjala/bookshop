from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50, help_text ='Enter your name')

    def __str__(self):
        return self.name

class Address(models.Model):
    town = models.CharField(max_length=50, help_text='Enter your Town')

    def __str__(self):
        return self.town

class Books(models.Model):
    title = models.CharField(max_length=50, help_text='Enter book Title')

    def __str__(self):
        return self.title

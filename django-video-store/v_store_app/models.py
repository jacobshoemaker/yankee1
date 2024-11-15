from django.db import models

class Client(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    account_type = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=30, null=False, blank=False)
    active = models.BooleanField(default=False)
    
class Video(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    in_stock = models.IntegerField(null=False, blank=False)
    rating = models.CharField(max_length=10, null=False, blank=False)

class Person(models.Model): 
    id = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    middle_init = models.CharField(max_length=2, null=False)
    age = models.IntegerField(null=False, blank=False)

class Address(models.Model): 
    id = models.IntegerField(primary_key=True, unique=True)
    street = models.CharField(max_length=100, null=False, blank=False)
    zipcode = models.BigIntegerField(null=False, blank=False)
    state = models.CharField(max_length=2, null=False, blank=False)
    apt_num = models.BigIntegerField(null=False, blank=False)
    
class Store(models.Model): 
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    number_of_employees = models.BigIntegerField(null=False, blank=False)
    rating = models.CharField(max_length=10, null=False, blank=False)
    owner = models.BigIntegerField(null=False, blank=False)  
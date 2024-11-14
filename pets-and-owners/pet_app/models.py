from django.db import models

# Create your models here.
class Owner(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    number_of_pets = models.IntegerField(default=1, null=False, blank=False)


class Cat(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    breed = models.CharField(max_length=255, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    vaccinated = models.BooleanField(null= False, default=False)
    description = models.TextField(max_length=255,null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)

class Dog(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    age = models.PositiveIntegerField(null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    vaccinated = models.BooleanField(null= False, default=False)
    breed = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=255,null=False, blank=False)
    
class bird(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    vaccinated = models.BooleanField(null= False, default=False)
    description = models.TextField(max_length=255,null=False, blank=False)
    species = models.CharField(max_length=255, null=False, blank=False)

class exotic_animal(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    region_of_origin = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    type_of_animal = models.CharField(max_length=255, null=False, blank=False)
    vaccinated = models.BooleanField(null= False, default=False)
    
    
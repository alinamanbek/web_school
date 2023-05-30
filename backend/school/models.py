
from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    experience = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    grade = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

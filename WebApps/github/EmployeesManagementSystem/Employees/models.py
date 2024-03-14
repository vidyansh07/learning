from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=255)
    discription = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    # Their my requirements are Name, Email, phone and department
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Login(models.Model):
    user_email = models.EmailField(primary_key=True)
    passworde = models.CharField(max_length=10,unique=True)
    
    def __str__(self):
        return self.user_email
    
class Expense(models.Model):
    user_email = models.ForeignKey(Login ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=100)
    date  = models.DateField(auto_now=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Income(models.Model):
    user_email = models.ForeignKey(Login,on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.source
    
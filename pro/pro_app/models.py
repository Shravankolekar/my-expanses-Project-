from django.db import models

# Create your models here.

class user_login(models.Model):
    emial=models.EmailField(max_length=1000)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class expancess(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    amount = models.BigIntegerField()
    note  = models.CharField(max_length=10000)
    expense_date = models.DateField( auto_now=True)
    payment_method = models.CharField(max_length=100)
    

    
    
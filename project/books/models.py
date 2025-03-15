from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']




class Book(models.Model):
    name = models.CharField(max_length=50, verbose_name="Title")
    author = models.CharField(max_length=30)
    date = models.DateField(verbose_name="Publishing Date", default=datetime.today())
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name="Cover")
    availability = models.BooleanField(default=True)
    Borrow = models.ForeignKey(User, on_delete=models.CASCADE,null = True,blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['category']
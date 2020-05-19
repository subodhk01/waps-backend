from django.db import models
from django.contrib.auth.models import User
from .choices import BORROWING,YEARS
import datetime


# Create your models here.
class Keyword(models.Model):
    key=models.CharField( max_length=30)

class Book(models.Model):
    title=models.TextField(max_length=50,
        blank=False,
        unique=False)
    author=models.TextField(max_length=32,blank=False)
    owner=models.ForeignKey(User, on_delete=models.CASCADE,related_name='User', null=True)
    
    description=models.TextField(max_length=512,blank=True)
    
    price=models.IntegerField(blank=False,default=0)
    #Borrowing method
    bMethod=models.CharField(max_length=1,choices=BORROWING)

    #status True means availabe
    borrowedBy=models.ForeignKey(User, on_delete=models.CASCADE,related_name='+',null=True)
    status=models.BooleanField(default=True)
    
    
    publication_year = models.IntegerField( choices=YEARS, default=datetime.datetime.now().year)
    cover=models.ImageField(blank=None, upload_to='./books/covers/', height_field=None, width_field=None, max_length=None)
    keywords=models.ManyToManyField(Keyword, related_name='keywords',null=True)










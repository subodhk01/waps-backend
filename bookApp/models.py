from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class keywords(models.Model):
    keyword=models.CharField( max_length=30),


class Book(models.Model):
    title=models.TextField(max_length=50,blank=False,unique=False)
    author=models.TextField(max_length=32,blank=False)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField(max_length=512,blank=True)
    borrowing_choice=(
        ('R','Rent'),
        ('S','Sell'),
        ('B','Both')
    )
    #Borrowing method
    bMethod=models.CharField(max_length=1,choices=borrowing_choice)
    #status True means availabe
    status=models.BooleanField(default=True)
    publication_date=models.DateField(null=True, auto_now=False)
    cover=models.URLField( max_length=200,blank=True)
    keyword=models.ManyToManyField(keywords)










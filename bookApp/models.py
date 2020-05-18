from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class keywords(models.Model):
    keyword=models.CharField( max_length=30),


class Book(models.Model):
    title=models.TextField(max_length=50,
        blank=False,
        unique=False)
    author=models.TextField(max_length=32,blank=False)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField(max_length=512,blank=True)
    borrowing_choice=(
        ('R','Rent'),
        ('S','Sell'),
        ('B','Both')
    )
    price=models.IntegerField(blank=False,default=0)
    #Borrowing method
    bMethod=models.CharField(max_length=1,choices=borrowing_choice)

    #status True means availabe
    borrowedBy=models.ForeignKey(User, on_delete=models.CASCADE,related_name='+',null=True)
    status=models.BooleanField(default=True)
    publication_date=models.DateField(null=True, auto_now=False)
    cover=models.ImageField(blank=None, upload_to='covers/', height_field=None, width_field=None, max_length=None)
    keyword=models.ManyToManyField(keywords)










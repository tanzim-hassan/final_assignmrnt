from django.db import models

# Create your models here.
class Car(models.model):
    car_name=models.models.CharField( max_length=110,unique=True)
    slug=models.SlugField(max_length=70,unique=True)
    description=models.TextField(max_length=200,blank=True)
    price=models.ImageField()
    images=models.ImageField(upload_to='photos/products')
    stock=models.ImageField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.models.DateTimeField(auto_now=True)
    


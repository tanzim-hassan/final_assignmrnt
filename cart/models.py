from django.db import models
from store.models import Car
from django.contrib.auth.models import User

# Create your models here.
class Cart(models.model):
    cart_id= models.CharField(max_length=300,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.cart_id

class CarItem(models.model):
    class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    product = models.ForeignKey(Car, on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.ImageField()
    is_active=models.BooleanField(default=True)
    def sub_total(self):
        return self.car.price*self.quantity
    def __str__(self):
        return self.car
    
    

from django.db import models

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=250,unique=True)
    car_image=models.ImageField(upload_to='photos/categoris',blank=True)

    def __str__(self) -> str:
        return self.category_name
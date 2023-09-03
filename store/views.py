from django.shortcuts import render
from .models import Car
from category.models import category

# Create your views here.
def store(request,category_slug=None):
    if category_slug:
      category=get_object_or_404(category,slug=category_slug)
      Car=Car.objects.filter(is_available=True,category=category)
    else:
        Car=Car.objects.filter(is_available=True)
        
    return render(request,'store/port.html')
def detail(request):
    return render (request,'store/detail.html',{'cars':Car})
    single_product=Car.objects.filter(slug=product_slug,category__slug=category_slug)

def CARnews(request):
    return render(request,'store/news.html')

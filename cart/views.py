from django.shortcuts import render,redirect
from store.models import Car
from .models import Cart,CarItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.

def cart(request):
     session_id=request.session.session_key
     cart_id=Cart.car.filter(cart_id=session_id).exists()
     if cart_id:
         cart_items=CarItem.objects.filter(cart=session_id)
          
     cart_items=CarItem.objects.filter
     return render(request,'cart/cart.html')
def add_to_cart(request,cart_id):
    current_user = request.user
    car=Car.objects.get(id=cart_id)
    if current_user.is_authenticated:
        is_cart_item_exists = CarItem.objects.filter(Car=Car, user=current_user).exists()
        if is_cart_item_exists:
            cart_items = CarItem.objects.filter(Car=Car, user=current_user)
            print(cart_items)
            item = CarItem.objects.get(Car=Car, user=current_user)
            item.quantity += 1
            item.save()
    session_id=request.session.session_key
    cart_id=cart.car.get(cart_id=session_id)
    if cart_id:
        cart_item=CarItem.car.filter(Car=car).exists()
        if cart_item:
           item=CarItem.car.get(Car=car)
           item.quantity+=1
           item.save()
    
            
           
        else:
            print('crt nai')
    else:
         cart=Cart.objects.create(
    cart_id= session_id
    )
    cart.save()

    
    cart.save()
    cart_item=CarItem.objects.create(
        Car=car
        quantity=1,
        cart=car

    )
    cart.save()
    return redirect('cart')
def remove_cart(request, Car_id, cart_item_id):

    Car = get_object_or_404(Car, id=Car_id)
    try:
        if request.user.is_authenticated:
            cart_item = CarItem.objects.get(Car=Car, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=cart_item_id(request))
            cart_item = CarItem.objects.get(Car=Car, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


def remove_cart_item(request, Car_id, cart_item_id):
    Car = get_object_or_404(Car, id=Car_id)
    if request.user.is_authenticated:
        cart_item = CarItem.objects.get(Car=Car, user=request.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=cart_item_id(request))
        cart_item = CarItem.objects.get(Car=Car, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CarItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=cart_item_id(request))
            cart_items = CarItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.Car.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass 

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'cart/cart.html', context)

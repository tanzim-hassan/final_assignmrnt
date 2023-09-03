from django.urls import path
from . import views
urlpatterns = [
    path('order/',views.order,name='order'),
    path('contact',views.contact,name='contact'),
       path('place_order/', views.place_order, name='place_order'),
    path('success/', views.success_view, name='success_view'),
]


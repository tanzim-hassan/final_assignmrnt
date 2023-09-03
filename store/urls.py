from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('detail/',views.detail,name='detail')
    path('news/',views.news,name='news')
    path('port/',views.port,name='port')
    
]
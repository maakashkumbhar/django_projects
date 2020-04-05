from django.contrib import admin
from django.urls import path
from foodsys import views
urlpatterns = [

    path('order',views.order,name='order'),
    path('Menu',views.Menu,name='Menu'),
    path('login',views.login,name='login'),
]

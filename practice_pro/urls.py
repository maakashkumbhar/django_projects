
from django.contrib import admin
from django.urls import path
from foodsys import views
from django.conf.urls import include

urlpatterns = [
    path('',views.home,name='home'),
    path('foodsys/',include('foodsys.urls')),
    path('admin/', admin.site.urls),
]

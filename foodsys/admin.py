from django.contrib import admin
from foodsys.models import New_User,User_login,Merchant,FoodItem

# Register your models here.
admin.site.register(New_User)
admin.site.register(User_login)
admin.site.register(Merchant)
admin.site.register(FoodItem)

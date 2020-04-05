from django.db import models

# Create your models here.
class New_User(models.Model):
    user_id = models.IntegerField()
    user_fname = models.CharField(max_length=264)
    user_lname = models.CharField(max_length=264)
    user_email = models.EmailField()
    user_address= models.CharField(max_length=264)
    user_contact = models.IntegerField()
    def __str__(self):
        return self.user_fname

class User_login(models.Model):
    email = models.ForeignKey(New_User,on_delete=models.CASCADE)
    password = models.CharField(max_length=264)

    def __str__(self):
        return self.user_id
class Merchant(models.Model):
    Merchant_id = models.IntegerField(unique=True)
    Merchant_name = models.CharField(max_length=264)
    Merchant_contact = models.IntegerField()
    Merchant_address = models.CharField(max_length=264)

    def __str__(self):
        return self.Merchant_name

class FoodItem(models.Model):
    FoodItem_id=models.IntegerField(unique=True)
    FoodItem_name = models.CharField(max_length=264)
    FoodItem_desc = models.CharField(max_length=264)

    def __str__(self):
        return self.FoodItem_name

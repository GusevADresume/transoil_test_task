from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    table_access= models.BooleanField()
    user_photo = models.ImageField()
    some_info = models.CharField(max_length=2500)

#TableUser
#123user*

class News(models.Model):

    news_header = models.CharField(max_length=50)
    news_body = models.CharField(max_length=500)
    news_image = models.ImageField()

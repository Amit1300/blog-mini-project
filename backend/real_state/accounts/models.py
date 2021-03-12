
from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Categories(models.TextChoices):
    WORLD = 'world'
    ENVIRONMENT = 'environment'
    TECHNOLOGY = 'technology'
    DESIGN = 'design'
    CULTURE = 'culture'


class BlogPost(models.Model):
    Author=models.CharField(max_length=50,default="author")
    user=models.ForeignKey(User ,related_name='blogs',on_delete=models.CASCADE ,default=1)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.WORLD)
    content = models.TextField(max_length=500)
    date_created =models.DateField( auto_now=False, auto_now_add=True)

   


    def __str__(self):
        return self.title
        



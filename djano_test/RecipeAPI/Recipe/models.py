from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    recipe_name=models.CharField(max_length=100)
    meal_type=models.CharField(max_length=100)
    cuisine=models.CharField(max_length=100)
    ingredients=models.TextField()
    instructions=models.TextField()
    image=models.ImageField(upload_to='Images',null=True)
    def __str__(self):
              return self.recipe_name

class Review(models.Model):
    comment=models.TextField()
    rating=models.FloatField()
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)
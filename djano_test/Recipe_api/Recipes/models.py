from django.db import models

# Create your models here.



class Recipe(models.Model):
         recipe_name = models.CharField(max_length=100)
         meal_type = models.CharField(max_length=100)
         cusine = models.CharField(max_length=100)
         ingredients = models.TextField(max_length=100)
         instructions = models.TextField(max_length=100)
         image = models.ImageField(upload_to='recipes',null=True)
from django.contrib import admin
from .models import ingredientItem, recipeItem
# Register your models here.
admin.site.register(ingredientItem)
admin.site.register(recipeItem)
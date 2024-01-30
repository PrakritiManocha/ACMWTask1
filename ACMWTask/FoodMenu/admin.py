from django.contrib import admin
from .models import UserProfile, FoodItem, Review

admin.site.register(UserProfile)
admin.site.register(FoodItem)
admin.site.register(Review)
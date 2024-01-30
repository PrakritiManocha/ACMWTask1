from django.urls import path
from .views import register, user_login, profile, home, review

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('profile/', profile, name='profile'),
    path('review/<int:food_item_id>/', review, name='review'),
]

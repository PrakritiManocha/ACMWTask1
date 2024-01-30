from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, ReviewForm, UserProfileForm
from .models import FoodItem, Review

def home(request):
    food_items = FoodItem.objects.all()
    return render(request, 'home.html', {'food_items': food_items})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    profile = user.userprofile if hasattr(user, 'userprofile') else None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})

@login_required
def review(request, food_item_id):
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.food_item_id = food_item_id
        review.save()
        return redirect('home')

    food_item = FoodItem.objects.get(pk=food_item_id)
    reviews = Review.objects.filter(food_item=food_item)
    return render(request, 'review.html', {'food_item': food_item, 'reviews': reviews, 'form': form})

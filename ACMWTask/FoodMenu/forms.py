from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile, Review
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    phone_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'address', 'phone_number', 'password1', 'password2')
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['food_item', 'comment']
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'address', 'phone_number')
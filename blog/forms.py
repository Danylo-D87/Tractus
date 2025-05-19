from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Post, Category, User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
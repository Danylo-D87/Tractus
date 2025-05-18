from django.views.generic import ListView

from django.shortcuts import render

from blog.models import Post, Category


def index(request):
    return render(request, "index.html")

from django.urls import path

from .views import (
    index,
    admin_tools_view,
    CategoryListView,
    CategoryDeleteView,
    CategoryUpdateView,
    CategoryCreateView,
    PostsListView,
    PostsDetailView,
    PostDeleteView,
    PostUpdateView,
    PostCreateView,
)

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("admin-tools/", admin_tools_view, name="admin-tools"),

    # Categories
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/add/", CategoryCreateView.as_view(), name="category-add"),
    path("categories/<int:pk>/edit/", CategoryUpdateView.as_view(), name="category-edit"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category-delete"),

    # Posts
    path("posts/", PostsListView.as_view(), name="posts-list"),  # всі пости
    path("posts/category/<str:category_name>/", PostsListView.as_view(), name="posts-by-category"),  # фільтр за категорією
    path("posts/add/", PostCreateView.as_view(), name="post-add"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("posts/<int:pk>/", PostsDetailView.as_view(), name="post-details"),
]


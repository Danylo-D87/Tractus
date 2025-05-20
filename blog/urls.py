from django.urls import path

from .views import (
    IndexView,
    AdminToolsView,
    ToggleLikeView,
    PopularPostsView,
    AboutAuthorsView,
    UserCreateView,
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
    path(
        "", IndexView.as_view(),
        name="index"
    ),
    path(
        "admin-tools/",
        AdminToolsView.as_view(),
        name="admin-tools"
    ),
    path(
        "posts/<int:post_id>/toggle-like/",
        ToggleLikeView.as_view(),
        name="toggle_like_api"
    ),
    path(
        "user/register/",
        UserCreateView.as_view(),
        name="user-create"
    ),
    path(
        "popular/",
        PopularPostsView.as_view(),
        name="popular_posts"
    ),
    path(
        "authors/",
        AboutAuthorsView.as_view(),
        name="about-authors"
    ),

    # Categories
    path(
        "categories/",
        CategoryListView.as_view(),
        name="category-list"
    ),
    path(
        "categories/add/",
        CategoryCreateView.as_view(),
        name="category-add"
    ),
    path(
        "categories/<int:pk>/edit/",
        CategoryUpdateView.as_view(),
        name="category-edit"
    ),
    path(
        "categories/<int:pk>/delete/",
        CategoryDeleteView.as_view(),
        name="category-delete"
    ),

    # Posts
    path(
        "posts/",
        PostsListView.as_view(),
        name="posts-list"
    ),
    path(
        "posts/category/<str:category_name>/",
        PostsListView.as_view(),
        name="posts-by-category"
    ),
    # фільтр за категорією
    path(
        "posts/add/",
        PostCreateView.as_view(),
        name="post-add"
    ),
    path(
        "posts/<int:pk>/edit/",
        PostUpdateView.as_view(),
        name="post-edit"
    ),
    path(
        "posts/<int:pk>/delete/",
        PostDeleteView.as_view(),
        name="post-delete"
    ),
    path(
        "posts/<int:pk>/",
        PostsDetailView.as_view(),
        name="post-details"
    ),
]

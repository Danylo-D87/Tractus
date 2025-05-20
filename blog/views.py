from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.views.generic import TemplateView, ListView

from blog.forms import (
    PostForm,
    CategoryForm,
    CustomUserCreationForm,
)
from blog.models import Category, Post, Like, User


class IndexView(TemplateView):
    template_name = "index.html"


@method_decorator(staff_member_required, name="dispatch")
class AdminToolsView(TemplateView):
    template_name = "admin_tools.html"


@method_decorator(login_required, name="dispatch")
class ToggleLikeView(View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like_qs = Like.objects.filter(post=post, user=request.user)
        if like_qs.exists():
            like_qs.delete()
            liked = False
        else:
            Like.objects.create(post=post, user=request.user)
            liked = True
        return JsonResponse({
            "liked": liked,
            "total_likes": post.likes.count()
            })


class PopularPostsView(ListView):
    model = Post
    template_name = "popular_posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.annotate(
            num_likes=Count("likes")
        ).order_by("-num_likes", "-created_at")


class AboutAuthorsView(TemplateView):
    template_name = "about_authors.html"


class UserCreateView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

class CategoryListView(generic.ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"


class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("blog:category-list")


class CategoryUpdateView(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("blog:category-list")


class CategoryDeleteView(generic.DeleteView):
    model = Category
    template_name = "category_confirm_delete.html"
    success_url = reverse_lazy("blog:category-list")


class PostsListView(generic.ListView):
    model = Post
    template_name = "posts_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.select_related("category", "author") \
                               .annotate(likes_count=Count("likes")) \
                               .order_by("-created_at")

        category_name = self.kwargs.get("category_name")
        if category_name:
            category = get_object_or_404(Category, name=category_name)
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["current_category"] = self.kwargs.get("category_name", "Всі категорії")
        context["user_is_authenticated"] = self.request.user.is_authenticated
        return context


class PostsDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_queryset(self):
        return Post.objects.annotate(likes_count=Count('likes')).select_related('author', 'category')


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_form.html"
    success_url = reverse_lazy("blog:posts-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(generic.UpdateView,):
    model = Post
    form_class = PostForm
    template_name = "post_form.html"
    success_url = reverse_lazy("blog:posts-list")


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("blog:posts-list")


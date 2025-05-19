from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404

from blog.forms import PostForm, CategoryForm
from blog.models import Category, Post


def index(request):
    return render(request, "index.html")


@staff_member_required
def admin_tools_view(request):
    return render(request, "admin_tools.html")


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
        queryset = Post.objects.select_related("category").order_by("-created_at")
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


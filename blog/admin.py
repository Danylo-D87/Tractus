from django.contrib import admin

from .models import User, Category, Tag, Post, Like


admin.site.site_header = "Tractus Admin"
admin.site.site_title = "Tractus Admin Portal"
admin.site.index_title = "Керування Tractus"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff")
    search_fields = ("username", "email")
    list_filter = ("is_staff",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('category', 'created_at', 'updated_at')
    raw_id_fields = ('author',)
    filter_horizontal = ('tags',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')
    search_fields = ('post__title', 'user__username')
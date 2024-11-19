# from django.contrib import admin
# from .models import Category, Thread, Post 

# # Register your models here
# admin.site.register(Category)
# admin.site.register(Thread)
# admin.site.register(Post)

from django.contrib import admin
from .models import Category, Thread, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'created_at', 'updated_at', 'image')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'thread', 'user', 'created_at', 'updated_at', 'image', 'total_likes')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'user', 'created_at')

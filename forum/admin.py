from django.contrib import admin
from .models import Category, Thread, Post  # Remove UserProfile

# Register your models here
admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Post)


# from django.contrib import admin
# from .models import UserProfile, Category, Topic, Post

# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'points')

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')

# @admin.register(Topic)
# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'created_by', 'created_at')

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('topic', 'created_by', 'created_at')

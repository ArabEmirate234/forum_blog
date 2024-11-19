# from django.db import models
# from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(blank=True, null=True)  # Optional description for each category

#     def __str__(self):
#         return self.name


# class Thread(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()  # Main content of the thread
#     category = models.ForeignKey(Category, related_name='threads', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)  # Tracks the last update time

#     def __str__(self):
#         return f"Thread: {self.title} by {self.user.username}"


# class Post(models.Model):
#     thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)  # Tracks the last update time

#     def __str__(self):
#         return f"Post by {self.user.username} on {self.thread.title}"

# from django.db import models
# from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField(blank=True, null=True)  # Optional description for each category
#     image = models.ImageField(upload_to='category_images/', blank=True, null=True)  # Image for the category

#     def __str__(self):
#         return self.name


# class Thread(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()  # Main content of the thread
#     category = models.ForeignKey(Category, related_name='threads', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)  # Tracks the last update time
#     image = models.ImageField(upload_to='thread_images/', blank=True, null=True)  # Optional image for the thread

#     def __str__(self):
#         return f"Thread: {self.title} by {self.user.username}"


# class Post(models.Model):
#     thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)  # Tracks the last update time
#     image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Optional image for the post

#     def __str__(self):
#         return f"Post by {self.user.username} on {self.thread.title}"
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # Optional description for each category
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)  # Image for the category

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()  # Main content of the thread
    category = models.ForeignKey(Category, related_name='threads', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Tracks the last update time
    image = models.ImageField(upload_to='thread_images/', blank=True, null=True)  # Optional image for the thread

    def __str__(self):
        return f"Thread: {self.title} by {self.user.username}"


class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Tracks the last update time
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)  # Optional image for the post
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)  # Track likes for the post

    def total_likes(self):
        """
        Return the total number of likes for the post.
        """
        return self.likes.count()

    def __str__(self):
        return f"Post by {self.user.username} on {self.thread.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on Post ID {self.post.id}"
    
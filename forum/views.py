# from django.shortcuts import render, redirect
# from django.views.generic import ListView
# from rest_framework import viewsets, filters
# from .models import Category, Thread, Post
# from .serializers import CategorySerializer, ThreadSerializer, PostSerializer
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login, logout
# from django.http import HttpResponseRedirect
# from django.urls import reverse


# # Regular Views
# def homepage(request):
#     """
#     Render the homepage with the latest categories, threads, and posts.
#     """
#     categories = Category.objects.all()
#     threads = Thread.objects.order_by('-created_at')[:5]  # Latest 5 threads
#     posts = Post.objects.order_by('-created_at')[:5]  # Latest 5 posts
#     return render(request, 'forum/homepage.html', {
#         'categories': categories,
#         'threads': threads,
#         'posts': posts,
#     })


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'forum/categories.html'
#     context_object_name = 'categories'


# class ThreadListView(ListView):
#     model = Thread
#     template_name = 'forum/threads.html'
#     context_object_name = 'threads'


# class PostListView(ListView):
#     model = Post
#     template_name = 'forum/posts.html'
#     context_object_name = 'posts'


# def login_view(request):
#     """
#     Handle user login functionality.
#     """
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return HttpResponseRedirect(reverse('homepage'))
#     else:
#         form = AuthenticationForm()
#     return render(request, 'forum/login.html', {'form': form})


# def logout_view(request):
#     """
#     Logs out the user and redirects to the homepage.
#     """
#     logout(request)
#     return redirect('homepage')  # Redirect to homepage after logout


# # API Viewsets
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all().order_by('name')
#     serializer_class = CategorySerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['name']


# class ThreadViewSet(viewsets.ModelViewSet):
#     queryset = Thread.objects.all().order_by('-created_at')
#     serializer_class = ThreadSerializer
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['title', 'category__name', 'user__username']
#     ordering_fields = ['created_at', 'title']


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all().order_by('-created_at')
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = ['content', 'thread__title', 'user__username']
#     ordering_fields = ['created_at']

from django.shortcuts import render, redirect
from django.views.generic import ListView
from rest_framework import viewsets, filters
from .models import Category, Thread, Post
from .serializers import CategorySerializer, ThreadSerializer, PostSerializer
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


# Regular Views
def homepage(request):
    """
    Render the homepage with the latest categories, threads, and posts.
    """
    categories = Category.objects.all()
    threads = Thread.objects.order_by('-created_at')[:5]  # Latest 5 threads
    posts = Post.objects.order_by('-created_at')[:5]  # Latest 5 posts
    return render(request, 'forum/homepage.html', {
        'categories': categories,
        'threads': threads,
        'posts': posts,
    })


class CategoryListView(ListView):
    """
    Render a list of all categories.
    """
    model = Category
    template_name = 'forum/categories.html'
    context_object_name = 'categories'


class ThreadListView(ListView):
    """
    Render a list of all threads.
    """
    model = Thread
    template_name = 'forum/threads.html'
    context_object_name = 'threads'


class PostListView(ListView):
    """
    Render a list of all posts.
    """
    model = Post
    template_name = 'forum/posts.html'
    context_object_name = 'posts'


def login_view(request):
    """
    Handle user login functionality.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = AuthenticationForm()
    return render(request, 'forum/login.html', {'form': form})


def logout_view(request):
    """
    Logs out the user and redirects to the homepage.
    """
    logout(request)
    return redirect('homepage')  # Redirect to homepage after logout


# API Viewsets
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing categories.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ThreadViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing threads.
    """
    queryset = Thread.objects.all().order_by('-created_at')
    serializer_class = ThreadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category__name', 'user__username']
    ordering_fields = ['created_at', 'title']


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for viewing and editing posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'thread__title', 'user__username']
    ordering_fields = ['created_at']

from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Thread, Post, Category
from .serializers import ThreadSerializer, PostSerializer, CategorySerializer

# API viewsets
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ThreadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows threads to be viewed or edited.
    """
    queryset = Thread.objects.all().order_by('-created_at')
    serializer_class = ThreadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category__name', 'user__username']
    ordering_fields = ['created_at', 'title']

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'thread__title', 'user__username']
    ordering_fields = ['created_at']

# Homepage view
def homepage(request):
    categories = Category.objects.all()
    threads = Thread.objects.order_by('-created_at')[:5]  # Display latest 5 threads
    posts = Post.objects.order_by('-created_at')[:5]      # Display latest 5 posts
    context = {
        'categories': categories,
        'threads': threads,
        'posts': posts,
    }
    return render(request, 'forum/homepage.html', context)

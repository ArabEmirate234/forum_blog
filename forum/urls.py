# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     homepage,
#     login_view,
#     logout_view,
#     CategoryListView,
#     ThreadListView,
#     PostListView,
#     CategoryViewSet,
#     ThreadViewSet,
#     PostViewSet,
# )

# # DRF Router for API Endpoints
# router = DefaultRouter()
# router.register(r'api/categories', CategoryViewSet, basename='api-categories')
# router.register(r'api/threads', ThreadViewSet, basename='api-threads')
# router.register(r'api/posts', PostViewSet, basename='api-posts')

# # URL Patterns
# urlpatterns = [
#     # HTML Views
#     path('', homepage, name='homepage'),
#     path('categories/', CategoryListView.as_view(), name='categories'),
#     path('threads/', ThreadListView.as_view(), name='threads'),
#     path('posts/', PostListView.as_view(), name='posts'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='account_logout'),

#     # API Endpoints
#     path('', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    homepage,
    login_view,
    logout_view,
    CategoryListView,
    ThreadListView,
    PostListView,
    CategoryViewSet,
    ThreadViewSet,
    PostViewSet,
)

# DRF Router for API Endpoints
router = DefaultRouter()
router.register(r'api/categories', CategoryViewSet, basename='api-categories')
router.register(r'api/threads', ThreadViewSet, basename='api-threads')
router.register(r'api/posts', PostViewSet, basename='api-posts')

urlpatterns = [
    # HTML Views
    path('', homepage, name='homepage'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('threads/', ThreadListView.as_view(), name='threads'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='account_logout'),

    # API Endpoints
    path('', include(router.urls)),  # API routes
]

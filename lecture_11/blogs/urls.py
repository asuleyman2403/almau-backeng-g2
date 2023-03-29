from django.urls import path
from blogs.views.cbv import ListCreateBlogAPIView, RetrieveUpdateDestroyBlogAPIView
from blogs.views.generics import PostsAPIView, RetrievePostAPIView, UpdatePostAPIView, DeletePostAPIView, PostAPIView, \
    BlogPostsAPIView

urlpatterns = [
    path('blogs/', ListCreateBlogAPIView.as_view()),
    path('blogs/<int:pk>/', RetrieveUpdateDestroyBlogAPIView.as_view()),
    path('blogs/<int:pk>/posts/', BlogPostsAPIView.as_view()),
    path('posts/', PostsAPIView.as_view()),
    path('posts/<int:pk>/', PostAPIView.as_view())
]


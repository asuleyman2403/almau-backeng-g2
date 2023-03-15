from django.urls import path
from blogs.views.fbv import list_create_blog
from blogs.views.cbv import ListCreateBlogAPIView, RetrieveUpdateDestroyBlogAPIView

urlpatterns = [
    # path('blogs', list_create_blog)
    path('blogs', ListCreateBlogAPIView.as_view()),
    path('blogs/<int:pk>', RetrieveUpdateDestroyBlogAPIView.as_view())
]


from django.urls import path
from blogs.views.cbv import ListCreateBlogAPIView, RetrieveUpdateDestroyBlogAPIView

urlpatterns = [
    path('', ListCreateBlogAPIView.as_view()),
    path('<int:pk>', RetrieveUpdateDestroyBlogAPIView.as_view())
]


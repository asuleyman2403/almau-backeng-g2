from rest_framework.decorators import api_view
from rest_framework.views import Response
from blogs.models import Blog, Post
from blogs.serializers import BlogSerializer, PostSerializer
from rest_framework import status
from datetime import datetime


@api_view(['GET', 'POST'])
def list_create_blog(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        data = request.data
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        serializer = BlogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



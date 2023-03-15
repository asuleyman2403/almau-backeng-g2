from rest_framework.views import APIView
from rest_framework.views import Response
from blogs.models import Blog, Post
from blogs.serializers import BlogSerializer, PostSerializer
from rest_framework import status
from datetime import datetime


class ListCreateBlogAPIView(APIView):

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        data['created_at'] = datetime.now()
        data['updated_at'] = datetime.now()
        serializer = BlogSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class RetrieveUpdateDestroyBlogAPIView(APIView):
    def get_blog(self, pk):
        try:
            blog = Blog.objects.get(id=pk)
            return blog
        except Blog.DoesNotExist:
            return None

    def get(self, request, pk):
        blog = self.get_blog(pk)
        if blog is None:
            return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data = request.data
        blog = self.get_blog(pk)
        if blog is None:
            return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = BlogSerializer(data=data, instance=blog)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        blog = self.get_blog(pk)
        if blog is None:
            return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            blog.delete()
            return Response({'message': 'Blog is deleted successfully!'}, status=status.HTTP_200_OK)


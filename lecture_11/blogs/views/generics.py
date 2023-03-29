from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView, RetrieveUpdateDestroyAPIView
from blogs.serializers import PostSerializer
from blogs.models import Post
from rest_framework.views import Response


class BlogPostsAPIView(ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Post.objects.filter(blog_id=pk)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['blog_id'] = kwargs['pk']
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class PostsAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class ListPostAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CreatePostAPIView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class RetrievePostAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UpdatePostAPIView(UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class DeletePostAPIView(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()




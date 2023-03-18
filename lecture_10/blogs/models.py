from django.db import models


class Blog(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(blank='', null=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    description = models.TextField(blank='', null=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

# blog.post_set.all()
# blog.posts.all()

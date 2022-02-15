from rest_framework import viewsets
from posts.models import Posts
from posts.api.serializers import PostsSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
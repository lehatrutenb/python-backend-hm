from rest_framework import viewsets, mixins
from .models import User, Comment, Post, MarkComment, MarkPost
from .serializers import UserSerializer, CommentSerializer, PostSerializer, MarkPostSerializer, MarkCommentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class MarkCommentViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    queryset = MarkComment.objects.all()
    serializer_class = MarkCommentSerializer

class MarkPostViewSet(mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                viewsets.GenericViewSet):
    queryset = MarkPost.objects.all()
    serializer_class = MarkPostSerializer
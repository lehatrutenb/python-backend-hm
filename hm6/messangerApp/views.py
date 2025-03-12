from django.db.models import Sum
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins
from .models import User, Comment, Post, MarkComment, MarkPost
from .serializers import UserSerializer, CommentSerializer, PostSerializer, MarkPostSerializer, MarkCommentSerializer, \
    MarksOnObjectSlimSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .slim_models import MarksOnObjectSlim
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__)

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

class CommentsOnPostAPIView(APIView):
    serializer_class = CommentSerializer

    def get(self, request, pk, format=None):
        try:
            Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(Comment.objects.filter(post=pk).all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostsOnUserAPIView(APIView):
    serializer_class = PostSerializer

    def get(self, request, pk, format=None):
        try:
            User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(Post.objects.filter(author=pk).all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SummaryMarkOnPostAPIView(APIView):
    serializer_class = MarksOnObjectSlimSerializer
    def get(self, request, pk, format=None):
        try:
            Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        mark_value = MarkPost.objects.filter(post=pk).aggregate(Sum('value', default=0))

        serializer = MarksOnObjectSlimSerializer(MarksOnObjectSlim(mark_value['value__sum'], pk))
        return Response(serializer.data, status=status.HTTP_200_OK)


class SummaryMarkOnCommentAPIView(APIView):
    serializer_class = MarksOnObjectSlimSerializer
    def get(self, request, pk, format=None):
        try:
            Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        mark_value = MarkComment.objects.filter(comment=pk).aggregate(Sum('value', default=0))

        serializer = MarksOnObjectSlimSerializer(MarksOnObjectSlim(mark_value['value__sum'], pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

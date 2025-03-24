from rest_framework import serializers
from .models import User, Comment, Post, MarkPost, MarkComment
from .slim_models import MarksOnObjectSlim


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class MarkPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkPost
        fields = '__all__'

class MarkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkComment
        fields = '__all__'

class MarksOnObjectSlimSerializer(serializers.Serializer):
    object_id = serializers.IntegerField()
    marks_value = serializers.IntegerField()

    def create(self, validated_data):
        return MarksOnObjectSlim(**validated_data)

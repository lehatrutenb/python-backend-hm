from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from messangerApp.models import *
from messangerApp.serializers import *
from django.contrib.auth.models import User as AuthUser
from django.core import serializers
import json
from django.test import TestCase

def login(client, user_ind: int):
    if user_ind == 1:
        client.login(username="test1", password="a12345678a")
    else:
        client.login(username="test2", password="a12345678a")

class TestMessangerServiceApi(APITestCase):
    def setUp(self):
        # dont want to depend on migration 0002
        User.objects.all().delete()
        Post.objects.all().delete()
        Comment.objects.all().delete()
        MarkPost.objects.all().delete()
        MarkComment.objects.all().delete()

        self.client = APIClient()
        self.auth_user1 = AuthUser.objects.create_user("test1", "test1@gmail.com", "a12345678a")
        self.auth_user2 = AuthUser.objects.create_user("test2", "test2@gmail.com", "a12345678a")
        self.user1 = User.objects.create(name="user1", auth_user_id=self.auth_user1.id)
        self.user2 = User.objects.create(name="user2", auth_user_id=self.auth_user2.id)
        self.post1 = Post.objects.create(title="title1", author=self.user1, published_date="2025-05-01", text="text1")
        self.post2 = Post.objects.create(title="title2", author=self.user2, published_date="2025-05-02", text="text2")
        self.comment1 = Comment.objects.create(author=self.user1, post=self.post1, published_date="2025-05-01", text="text1")
        self.comment2 = Comment.objects.create(author=self.user2, post=self.post1, published_date="2025-05-02", text="text2")
        self.mark_post1 = MarkPost.objects.create(author=self.user1, post=self.post1, value=3)
        self.mark_post2 = MarkPost.objects.create(author=self.user2, post=self.post1, value=-2)
        self.mark_comment1 = MarkComment.objects.create(author=self.user1, comment=self.comment1, value=3)
        self.mark_comment2 = MarkComment.objects.create(author=self.user2, comment=self.comment1, value=-2)

    def test_comments_on_post_get(self):
        url = '/api/messanger/comments_on_post/{}/'.format(self.post1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([comment["id"] for comment in response.json()], [self.comment1.id, self.comment2.id])

    def test_posts_on_user_get(self):
        url = '/api/messanger/posts_on_user/{}/'.format(self.user1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([post["id"] for post in response.json()], [self.post1.id])

    def test_summary_mark_comment_get(self):
        url = '/api/messanger/summary_mark_comment/{}/'.format(self.comment1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["marks_value"], 1)

    def test_summary_mark_comment_get(self):
        url = '/api/messanger/summary_mark_post/{}/'.format(self.post1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["marks_value"], 1)

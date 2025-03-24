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

class TestUserApi(APITestCase):
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

    def test_user_get(self):
        url = '/api/messanger/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([user["id"] for user in response.json()], [self.user1.id, self.user2.id])

    def test_user_get_one(self):
        url = '/api/messanger/users/{}/'.format(self.user1.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["id"], self.user1.id)

    def test_user_post(self):
        url = '/api/messanger/users/'
        data = {
            "id": 1303, # check that id can't be set by request
            "name": "leha",
            "auth_user": self.auth_user1.id
        }
        login(self.client, 1)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = '/api/messanger/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([user["name"] for user in response.json()], [self.user1.name, self.user2.name, "leha"])

    def test_user_patch(self):
        url = '/api/messanger/users/{}/'.format(self.user1.id)
        data = {
            "name": "leha",
        }
        login(self.client, 1)
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = '/api/messanger/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([user["name"] for user in response.json()], ["leha", self.user2.name])

    def test_user_put(self):
        url = '/api/messanger/users/{}/'.format(self.user1.id)
        data = {
            "name": "leha",
            "auth_user": self.auth_user1.id
        }
        login(self.client, 1)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = '/api/messanger/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([user["name"] for user in response.json()], ["leha", self.user2.name])

    def test_user_delete(self):
        url = '/api/messanger/users/{}/'.format(self.user1.id)
        login(self.client, 1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        url = '/api/messanger/users/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([user["name"] for user in response.json()], [self.user2.name])

    def test_auth_required(self):
        url = '/api/messanger/users/{}/'.format(self.user1.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = '/api/messanger/users/{}/'.format(self.user1.id)
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = '/api/messanger/users/{}/'.format(self.user1.id)
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = '/api/messanger/users/{}/'.format(self.user1.id)
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_required_another_user(self):
        login(self.client, 2)
        url = '/api/messanger/users/{}/'.format(self.user1.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = '/api/messanger/users/{}/'.format(self.user1.id)
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = '/api/messanger/users/{}/'.format(self.user1.id)
        data = {
            "name": "leha",
            "auth_user": self.auth_user1.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

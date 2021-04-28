import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user.factories import UserFactory
from user.models import User


class BaseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.ru', name='test', password='pass')
        # self.client.login(email='test@test.ru', password='pass')


class TestUser(BaseTestCase):
    def test_create_user(self):
        response = self.client.post(
            reverse('user_registration'),
            data=json.dumps({
                "email": 'new_test@example.com',
                "nickname": 'test',
                "password": '12345678',
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_login(self):
        response = self.client.post(
            reverse('user_login'),
            data=json.dumps({
                "email": 'test@test.ru',
                "password": 'pass',
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_get_user(self):
        user = UserFactory()
        response = self.client.get(
            reverse('user', args=[user.id]),
            HTTP_AUTHORIZATION=f"Bearer {user.access}",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        user = UserFactory()
        response = self.client.put(
            reverse('user', args=[user.id]),
            data=json.dumps({
                "fb": 'https://fb.com/',
                "nickname": 'test',
                "google_play": "google.ru",
                "game_center": "game_center.ru",
            }),
            content_type='application/json',
            HTTP_AUTHORIZATION=f"Bearer {user.access}",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refrash_token(self):
        user = UserFactory()
        response = self.client.post(
            reverse('user_refresh'),
            data=json.dumps({
                "refresh": user.refresh,
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)

import email
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from sections.models import Section


class AuthTests(APITestCase):
    def test_login(self):
        data = {
            "email": "za@za.com",
            "password1": "za@123456",
            "password2": "za@123456",
        }
        response = self.client.post("/dj-rest-auth/registration/", data, format="json")
        data = {"email": "za@za.com", "password": "za@123456"}
        response = self.client.post("/dj-rest-auth/login/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SectionTests(APITestCase):
    def create_token(self):
        user = User(email="za@za.com", password="za")
        user.save()
        token = Token.objects.create(user=user)
        return token.key

    def test_get_section(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.create_token())
        response = self.client.get("/api/v1/sections/", format="json")
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_section(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.create_token())
        data = {"title": "test", "body": "test"}
        response = self.client.post("/api/v1/sections/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_section(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.create_token())
        section = Section(title="test", body="test", owner=User.objects.get(id=1))
        section.save()
        response = self.client.delete("/api/v1/sections/1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

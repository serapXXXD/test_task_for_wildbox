from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

urls_list = [f'https://www.youtube.com/watch?v=w4305iB8LBs&t={i}s' for i in range(1, 2002, 100)]
json_urls_list = {'url_list': urls_list}
print(json_urls_list)


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_user_1 = User.objects.create_user(username='user99', password='Qq123456')
        cls.test_user_1.save()
        cls.unauthorized_api_client = APIClient()
        cls.test_user_1_api_client = APIClient()
        cls.test_user_1_api_client.force_authenticate(cls.test_user_1)


class TestWorkWithUrlsUnauthorizedClient(BaseTest):

    def test_get_request_unauthorized_client(self):
        response = self.unauthorized_api_client.get('/api/urls/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_current_url_request_unauthorized_client(self):
        response = self.unauthorized_api_client.get('/api/urls/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_request_unauthorized_client_single_url(self):
        response = self.unauthorized_api_client.post(path='/api/urls/', data={'url': urls_list[0]})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.unauthorized_api_client.post(path='/api/urls/', data={'url': urls_list[5]})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_request_unauthorized_client_list_urls(self):
        response = self.unauthorized_api_client.post(path='/api/urls/bulk_create/', data=json_urls_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_request_unauthorized_client(self):
        response = self.unauthorized_api_client.get('/api/urls/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestWorkWithUrlsAuthorizedClient(BaseTest):
    def test_get_request(self):
        response = self.test_user_1_api_client.get('/api/urls/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_request_single_url(self):
        response = self.test_user_1_api_client.post(path='/api/urls/', data={'url': urls_list[0]})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['url'], urls_list[0])

    def test_post_request_bulk_create(self):
        response = self.test_user_1_api_client.post(path='/api/urls/bulk_create/', data=json_urls_list)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for count, url in enumerate(response.json()['url_list']):
            self.assertEqual(url['url'], urls_list[count])


"""
тестю добавление урлов
и работу эндпоинтов
"""

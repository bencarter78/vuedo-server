from django.test import TestCase, Client
from api.models import List
from http import HTTPStatus

class TestListController(TestCase):
    def test_it_returns_all_lists(self):
        List.objects.create(name="Shopping", icon="example-icon")
        List.objects.create(name="Diy", icon="example-icon")
        
        response = Client().get('/api/lists')

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual(2, len(response.json()['data']))
        self.assertEqual('John', response.json()['data'])


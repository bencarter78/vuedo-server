from django.test import TestCase
from api.models import List

class TestModels(TestCase):
    def test_a_list_has_a_name(self):
        listA = List.objects.create(name='Shopping', icon='example-icon')
        self.assertEqual('Shopping', listA.name)

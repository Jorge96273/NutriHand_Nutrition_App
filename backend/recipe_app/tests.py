from django.test import TestCase
from unittest.mock import patch
from rest_framework.test import APIClient
from django.urls import reverse
import json


class RecipeProjectTest(TestCase):
    # make class attributes in the setUp method and is triggered before every class
    def setUp(self):
        self.client = APIClient()

    @patch("requests.get")
    def test_something(self, mock_get):
        nut ='Iron'
        preview_url = "https://something"
        mock_response = type("MockResponse",(), {"json": lambda self: {"title": preview_url}})
        mock_get.return_value = mock_response()
        response = self.client.get(reverse("search_nutrient",args=[nut]))
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), preview_url)

        
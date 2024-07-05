from django.test import TestCase
from django.shortcuts import reverse

class HomePagetest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse("landing"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, "navbar.html")

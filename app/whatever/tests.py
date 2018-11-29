from django.test import TestCase
from django.urls import reverse

from whatever.models import Whatever
from django.utils import timezone


# models test
class WhateverTest(TestCase):
    def create_whatever(self, title="only a test", body="yes, this is only a test"):
        return Whatever.objects.create(title=title, body=body, created_at=timezone.now())

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, Whatever))
        self.assertEqual(w.__unicode__(), w.title)

    def test_whatever_list_view(self):
        w = self.create_whatever()
        url = reverse('whatever.views.whatever')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(w.title, response.content.decode('utf-8'))


import os
import unittest
from selenium import webdriver


class TestSignup(unittest.TestCase):
    def setUp(self):
        current_folder = os.path.dirname(os.path.realpath(__file__))
        driver_path = os.path.join(current_folder, 'chromedriver')
        self.driver = webdriver.Chrome(driver_path)

    def test_signup_fire(self):
        self.driver.get("http://localhost:8000/add/")
        self.driver.find_element_by_id('id_title').send_keys("test title")
        self.driver.find_element_by_id('id_body').send_keys("test body")
        self.driver.find_element_by_id('submit').click()
        self.assertIn("http://localhost:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

from django.test import TestCase
from django.urls import reverse

from whatever.forms import WhateverForm
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

    def test_valid_form(self):
        w = Whatever.objects.create(title='Foo', body='Bar')
        data = {'title': w.title, 'body': w.body}
        form = WhateverForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Whatever.objects.create(title='Foo', body='')
        data = {'title': w.title, 'body': w.body}
        form = WhateverForm(data=data)
        self.assertFalse(form.is_valid())


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

from tastypie.test import ResourceTestCaseMixin


class EntryResourceTest(ResourceTestCaseMixin, TestCase):
    def test_get_api_json(self):
        resp = self.api_client.get('/api/whatever/', format='json')
        self.assertValidJSONResponse(resp)

    def test_get_api_xml(self):
        resp = self.api_client.get('/api/whatever/', format='xml')
        self.assertValidXMLResponse(resp)

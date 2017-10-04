# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import resolve
from views import landing

# Create your tests here.
class TripTest(TestCase):
    """Test that landing view is stuff!"""

    def test_landing_endpoint(self):
        """Tests that root url goes to landing page"""
        endpoint = resolve("/")
        print(endpoint)
        self.assertEquals(endpoint.func, landing)


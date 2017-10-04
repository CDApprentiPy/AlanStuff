# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import resolve
from views import main 

# Create your tests here.
class EzTests(TestCase):

    def test_getstolanding(self):
        response = resolve('/')
        self.assertEquals(response.func, main)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import resolve
from views import main

# Create your tests here.
# test a view function is found!
class TesterThing(TestCase):
    def test_home_loads(self):
        found = resolve('/')
        print(found)
        print(main)
        self.assertEquals(found.func, main)
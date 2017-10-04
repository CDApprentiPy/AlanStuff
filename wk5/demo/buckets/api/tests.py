# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import BucketList

# Create your tests here.
class ModelTestCase(TestCase):
    """this thing tests modelstuff!"""
    def setUp(self):
        """get test client all set up:D"""
        self.bucketlist_name = "Write good code"
        self.bucketlist = BucketList(name=self.bucketlist_name)
    
    def test_model_can_create_a_bucketlist(self):
        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """For testing them views yo!"""
    def setUp(self):
        """Define the test case and set up le things"""
        self.client = APIClient()
        self.bucketlist_data = { 'name': "go to ibiza"}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format='json')
    
    def test_api_can_create_a_bucketlist(self):
        """Test the api can create a bucket! pls pls pls!"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        bucketlist = BucketList.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': bucketlist.id},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, BucketList)
    
    def test_api_can_update_bucketlist(self):
        change_bucketlist = {'name': 'something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json',
        )
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        bucketlist = BucketList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format="json",
            follow=True,
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
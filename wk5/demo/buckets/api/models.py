# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BucketList(models.Model):
    """This is the bucketlist!!!"""
    name = models.CharField(max_length=255, blank=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """I Liek U Tu Reed Gud"""
        return"{}".format(self.name)
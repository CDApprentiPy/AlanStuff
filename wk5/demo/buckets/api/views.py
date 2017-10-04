# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketSerializer
from .models import BucketList

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """This class defines the behavior of your restful api"""
    queryset = BucketList.objects.all()
    serializer_class = BucketSerializer

    def perform_create(self, serializer):
        """Save the post Datas! when createing"""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Handles the not crete stuff"""
    queryset = BucketList.objects.all()
    serializer_class = BucketSerializer
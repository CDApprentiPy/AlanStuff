# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import forms

# Create your views here.
def main(request):
    "takes you to log/reg page"
    context = {
        'logform': forms.LogForm,
        'regform': forms.RegForm
    }
    return render(request, 'logg/main.html', context)
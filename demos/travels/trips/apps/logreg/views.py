# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from forms import RegForm

# Create your views here.
def landing(request):
    """Takes us to logreg!"""
    context = {
        'regform': RegForm(),
    }
    template = 'logreg/landing.html'
    return render(request, template, context)

def create(request):
    """Creates a user"""
    form = request.POST
    print("you sucesful routed")
    if form.is_valid():
        print("Form is G!!!")
        context = {
            'users': User.objects.all(),
        }
        return render(request, 'landing/dashboard.html', context)
    else:
        print("form was not valid, por quoi?")
        return redirect(reverse('/'))
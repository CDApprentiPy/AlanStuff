# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponseRedirect, reverse

# Create your views here.
def index(request):
    context = {}
    if 'golds' not in request.session:
        print("inserting things in session")
        request.session['golds'] = 0
    context = {
        'golds': request.session['golds'],
    }
    print context['golds']
    return render(request, 'golds/index.html', context)

def process(request):
    activity = request.POST['activity']
    print(activity)
    new_gold = request.session['golds']+14
    print new_gold
    context = {
        'golds': new_gold,
    }
    request.session['golds'] = new_gold
    return redirect('/')
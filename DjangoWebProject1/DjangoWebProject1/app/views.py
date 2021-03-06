﻿"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import *
from django.db.models.query import QuerySet

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def Test(request, id):
    """
    :type id: int
    """
    assert isinstance(request, HttpRequest)
    #assert isinstance(request, int)
    #from django.core.management import call_command
    #call_command('migrate')
    #call_command('makemigrations', 'myapp', verbosity=3, interactive=False)
    #call_command('migrate', 'myapp', verbosity=3, interactive=False)

    Test = QuerySet
    Test = Company.objects

    Record = Company()
    Record = Test.get(id = id)

    return render(
        request,
        'app/Test.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'Person': Record,
            'IsCustomerIsValid': False,
            'Test' : '<h3>Hello World</h3>' 
        })
    )

def Bacon(request):
    """
    :type id: int
    """
    assert isinstance(request, HttpRequest)
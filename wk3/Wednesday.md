# Wednesday!
Wednesday:
    - Algorithms
        - Topic: 
    - AM Lecture
        - Topic: BCrypt/Validations/Named Routes/Namespaces
        - Group Activity: LogReg :D, or at least add users to a db
    - PM Lecture
        - Topic:
        - Group Activity:
    - EOD:

## Lectures
-AM:
    - Validations + Named Routes
    - Validations
        - Where does this business happen?
            - Models!
            - What is it that manages our models?
                - Managers! woot!
                - How do we extend this business?
            - Can our models talk to our views?
        - BCrypt
            - 
    - Named Routes
        - Why?
            - DRY!
        - How?
            - in urls.py:
                - url(r'somehting/something', views.does_stuff, name='doesthings')
            - in views.py:
                - redirect('doesthings')
            - in something.html
                - {%url 'my_view_method' kwars=values %}
        - Multiple apps?
            - use a namespace to distinguish your things
                - what is a namespace?
            - add namespace when you use include statement
            - basically, add 'appname:method'
    - Reverse https://docs.djangoproject.com/en/1.11/ref/urlresolvers/#django.urls.reverse


        - What!Why?
            - what happens when we redirect for our url?
            - how can we 'rebuild' a url?
        - How:
            - in python:
                - reverse()
            - in templates: 
                - {% url 'app:route' %}
    - forms
        - https://docs.djangoproject.com/en/1.11/topics/forms/
        - create a subclass of django's built in form class from django import forms
            - if a form is an object/class, what might it's fields be?
                - inputs
                    - can give them validations, types, widgets
                - methods
                    - isValid?
            - how to render? well, its a django object so we gotta pass it to templates
                - in templates:
                    - can render a few ways
                        {{form.as_p/table/ul}}
                        unpack manually
    - Group Activity:
        - Survey Form
            - 2 apps, one that has the form? <- didnt use this last time
            - separate one for the      
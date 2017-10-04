Lecture things

some code from IRL: https://github.com/mozilla/bedrock/blob/master/bedrock/firefox/views.py

Start: Lets talk about forms! but first, we need a model to wokr with
So lets just make a generic user, we do this a lot good thing django has a built in User class that wecan use!
    - Intro to User class
        - purpose
            - built in django tool to help with authorization and permissionsing
        - features
            - some built in fields!
            - some built in methods!
        - basic how to use
            - how do i add fields?
            - generally, just add a 1:1 to something called a profile!
        - advanced how to use
            - you can use it to do permissions
    - Instantiate a basic User+Profile combo
        - Why?
            - use the user model
        - How?
            - 
Sweet, but what if I want to make some Users? Withour building a form yet?
    - Intro to the Admin site! what!
    - What can it do for us?
        - model-centric interface for your application
    - __repr__ in User model to see how it is represented in admin
        - how?
            in models __unicode__ or __stirng__
            - https://stackoverflow.com/questions/9336463/django-xxxxxx-object-display-customization-in-admin-action-sidebar
    - register user model as something to be registered in admin
        - how?
            if you dont want to spiff up admin model, admin.site.register(Model) in admin.py
            if you want to spiff it up define an AdminModel and you can do it ^way or with decorator
Better make a page to show a form to make a user... Class Based Views what!
    - basic use...TemplateView
    - what/WHY/how
        - why?
            - A view simply accepts a request and returns a response, many of them do pretty much the same thing, so django has supplied some pre-built things where we just have to provide the context information
            - why handle post/get
            - https://simpleisbetterthancomplex.com/article/2017/03/21/class-based-views-vs-function-based-views.html
        - what
            - templateviews, redirectviews, detail + list views, etc.
    - How?
        - views have as_view()method
        - create class, call it as view
            - tell it what its context is?
Cool, but what about forms?

    - i mean most of our forms are just to collect model info, are we duplicating code with form and model validations?
    - How to use model-based forms! https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/
        - model form, have to tell it which fields to show and which model to be based off of
        - Fun validations
            - https://stackoverflow.com/questions/34609830/django-modelform-how-to-add-a-confirm-password-field

    - Lets talk about forms and meta now
        - https://docs.djangoproject.com/en/1.11/topics/forms/
        - Form life-cycle things
            - clean
            - is_clean
            - is_valid
        - what is a meta tag?
    - passing data to the form/instantiating one
        - 

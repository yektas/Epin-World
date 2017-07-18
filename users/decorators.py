from django.shortcuts import redirect, render_to_response


def is_admin(func):
    """ This decorator checks whether the user is an admin or not.
        If the user is not admin redirects to login page """
    ''' Sercan : 15.07.2017 '''
    def wrap(request, *args, **kwargs):
        if 'admin_id' not in request.session or request.session['admin_id'] == 2:
            return redirect("users:login")
        else:
            return func(request, *args, **kwargs)
    return wrap


def language_assigned(func):
    """ This decorator sets the language in COOKIES object according to user's choice
        If the language is not selected, assigns Turkish as default. """
    ''' Sercan : 17.07.2017 '''
    def wrap(request, *args, **kwargs):
        if 'language' not in request.COOKIES:
            request.COOKIES['language'] = 'tr'
            response = render_to_response("{}/index.html".format(request.COOKIES['language']))
            response.set_cookie('language', '{}'.format(request.COOKIES['language']))
            return func(request, *args, **kwargs)
        else:
            return func(request, *args, **kwargs)
    return wrap


def login_required(func):
    """ This decorator checks whether the user is logged in or not.
        If the user is not logged in redirects to login page """
    ''' Sercan : 15.07.2017 '''
    def wrap(request, *args, **kwargs):
        if 'is_logged' not in request.session or request.session['is_logged'] == False:
            return redirect("users:login")
        else:
            return func(request, *args, **kwargs)
    return wrap
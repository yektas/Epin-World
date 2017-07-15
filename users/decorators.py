from django.shortcuts import redirect


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
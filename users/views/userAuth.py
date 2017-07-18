from django.shortcuts import redirect

from users.decorators import language_assigned
from users.models import UserEventClass


@language_assigned
def auth_login(request):
    """ Login Authentication: gets the user's username and password
      from the html form with POST method and checks the database,
      if user exists, username, password and is_logged variables are
      passed to the session. Then redirects to the index page.
      if user does not exits reloads the login page """
    ''' Sercan : 11.07.2017 '''
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user_info = request.POST

        instance = UserEventClass(user_info)
        instance.update_lastlogin(username)
        user = instance.login_event()

        if len(user) > 0:
            request.session['admin_id'] = user[0]['admin_id']
            request.session['username'] = username
            request.session['password'] = password
            request.session['is_logged'] = True

            return redirect("users:index")

        else:
            return redirect("users:login")

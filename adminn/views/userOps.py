import datetime
import logging

from django.shortcuts import render, redirect

from users.decorators import language_assigned, is_admin
from users.models import UserEventClass


@language_assigned
# @is_admin
def user_list(request):
    """ Lists all users in admin panel """
    ''' Sercan : 13.07.2017 '''
    instance = UserEventClass(request)
    users = instance.list_users()
    return render(request, "{}/userlist.html".format(request.COOKIES['language']), {'users': users})


@language_assigned
@is_admin
def delete_user(request):
    """ Deletes user """
    ''' Sercan : 13.07.2017 '''
    request.POST.get()
    instance = UserEventClass(request)
    instance.delete_user()
    logging.info('User deleted.'.format(datetime.datetime.now()))
    return redirect("adminn:user_list")


@language_assigned
@is_admin
def ordertable(request):
    return render(request, "{}/ordertable.html".format(request.COOKIES['language']),
                  {'lang_data': request.COOKIES['language']})

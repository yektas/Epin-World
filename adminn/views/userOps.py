import datetime
import logging

from django.shortcuts import render, redirect

from adminn.models.userModels import UserOperationClass
from utility.decorators import language_assigned, is_admin

logging.basicConfig(filename= 'debug.log' , level= logging.DEBUG)


@language_assigned
# @is_admin
def user_list(request):
    """ Lists all users in admin panel """
    ''' Sercan : 13.07.2017 '''
    instance = UserOperationClass(request)
    users = instance.list_users()
    logging.info('users listed / {}'.format(datetime.datetime.now()))
    return render(request, "{}/userlist.html".format(request.COOKIES['language']), {'users': users})


@language_assigned
# @is_admin
def delete_user(request):
    """ Deletes user """
    ''' Sercan : 13.07.2017 '''
    request.POST.get()
    instance = UserOperationClass(request)
    instance.delete_user()
    logging.info('User deleted.'.format(datetime.datetime.now()))
    return redirect("adminn:user_list")


@language_assigned
# @is_admin
def order_table(request):
    return render(request, "{}/ordertable.html".format(request.COOKIES['language']),
                  {'lang_data': request.COOKIES['language']})


@is_admin
@language_assigned
def ban_user(request):
    """Postdan aldigimiz useri statusunu değistirip yasakliyoruz"""
    if request.method == "POST":
        uname = request.POST.get('name', '')
        instance = UserOperationClass(request)
        instance.ban_user(uname)
        logging.info('user banned. / {}'.format(datetime.datetime.now()))
        return redirect("adminn:user_list")
    else:
        return redirect("adminn:user_list")

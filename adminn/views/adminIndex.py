import logging

from django.shortcuts import render

from utility.decorators import language_assigned

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

@language_assigned
# @is_admin
def admin_index(request):
    logging.info("ADMIN PANEL viewed.!")
    return render(request, "{}/admin.html".format(request.COOKIES['language']))

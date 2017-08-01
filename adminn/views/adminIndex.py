import logging

from django.shortcuts import render

from utility.decorators import is_admin

logging.basicConfig(filename='debug.log', level=logging.DEBUG)


@is_admin
def admin_index(request):
    logging.info("ADMIN PANEL viewed.!")
    return render(request, "admin.html")

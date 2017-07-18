import datetime
import logging

from django.shortcuts import redirect, render

from adminn.models import AdminEventClass
from users.decorators import language_assigned

models = AdminEventClass()


@language_assigned
# @is_admin
def create_company(request):
    if request.method == "POST":
        name = request.POST.get('cname', ' ')
        if (models.create_company(name)):
            logging.info('company created'.format(datetime.datetime.now()))
            return redirect("adminn:admin_index")

    return render(request, "{}/company.html".format(request.COOKIES['language']))


@language_assigned
# @is_admin
def list_company(request):
    company = models.list_company()
    return render(request, "{}/companylist.html".format(request.COOKIES['language']), {"company": company})

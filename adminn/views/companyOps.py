import datetime
import logging

from django.shortcuts import redirect, render

from adminn.models.companyModels import CompanyEventClass
from utility.decorators import language_assigned


@language_assigned
# @is_admin
def create_company(request):
    instance = CompanyEventClass(request)
    if request.method == "POST":
        name = request.POST.get('cname', ' ')
        if instance.create_company(name):
            logging.info('company created'.format(datetime.datetime.now()))
            return redirect("adminn:admin_index")

    return render(request, "{}/company.html".format(request.COOKIES['language']))


@language_assigned
# @is_admin
def list_company(request):
    instance = CompanyEventClass(request)
    company = instance.list_company()
    return render(request, "{}/companylist.html".format(request.COOKIES['language']), {"company": company})

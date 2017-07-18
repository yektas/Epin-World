from django.shortcuts import render

from adminn.models import AdminEventClass
from users.decorators import language_assigned

models = AdminEventClass()


@language_assigned
# @is_admin
def admin_index(request):
    return render(request, "{}/admin.html".format(request.COOKIES['language']))

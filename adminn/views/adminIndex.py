from django.shortcuts import render

from utility.decorators import language_assigned


@language_assigned
# @is_admin
def admin_index(request):
    return render(request, "{}/admin.html".format(request.COOKIES['language']))

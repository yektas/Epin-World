from django.conf.urls import url

from adminn.views import adminIndex, gameOps, userOps, companyOps

app_name = 'adminn'

urlpatterns = [

    url(r'^$', adminIndex.admin_index, name='index'),
    url(r'^createcompany/$', companyOps.create_company, name='create_company'),
    url(r'^listcompany/$', companyOps.list_company, name='list_company'),
    url(r'^listgame/$', gameOps.list_game, name="list_game"),
    url(r'^addgame/$', gameOps.add_game, name='add_game'),
    url(r'^deletegame/$', gameOps.delete_game, name='delete_game'),
    url(r'^userlist/$', userOps.user_list, name='user_list'),
    url(r'^deleteuser/$', userOps.delete_user, name='delete_user'),
    url(r'^ordertable/$', userOps.order_table, name='order_table'),
]

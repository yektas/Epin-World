from django.conf.urls import url
from adminn import views

app_name = 'adminn'

urlpatterns = [

url(r'^$', views.admin_index, name='index'),
url(r'^createcompany/$' , views.create_company, name='createcomp'),
url(r'^listcompany/$', views.list_company, name='listcompany'),
url(r'^creategame/$', views.create_game, name="creategame"),
url(r'^listgame/$', views.list_game, name="listgame"),




        ]
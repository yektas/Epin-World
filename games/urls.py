from django.conf.urls import url
from games import views

app_name = 'games'

urlpatterns = [
    #url(r'^(?P<game_name>[\w-]+)/$', views.games,name= 'games'),
    url(r'^detail/$', views.detail,name= 'detail'),
    url(r'^games_json/$', views.games_json, name='games_json'),

]
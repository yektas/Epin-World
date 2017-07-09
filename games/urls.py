from django.conf.urls import url
from games import views

app_name = 'games'

urlpatterns = [
    url(r'^(?P<game_name>[\w-]+)/$', views.games,name= 'games'),
]
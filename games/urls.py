from django.conf.urls import url

from games.views import views

app_name = 'games'

urlpatterns = [
    url(r'^games_json/$', views.games_json, name='games_json'),
    url(r'^game_detail_search/$', views.generate_detail_html, name="detail_search"),
    url(r'^game_detail/(?P<game_name>\w+)$', views.generate_detail_html),
    url(r'^search/$', views.SearchView, name="search_game"),

]
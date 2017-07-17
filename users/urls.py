from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^auth_login/$', views.auth_login, name='auth_login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^admin/$', views.adminview, name='adminview'),
    url(r'^oyunekle/$', views.oyunekle_first, name='oyunekle'),
    url(r'^oyunsil/$', views.oyunsil, name='oyunsil'),
    url(r'^userslist/$', views.user_list, name='user_list'),
    url(r'^deleteuser/$', views.delete_user, name='delete_user'),
    url(r'^company/$', views.companylist, name='company'),
    url(r'^companyy/$', views.company, name='companyy'),
    url(r'^ordertable/$', views.ordertable, name='ordertable'),
    url(r'^create_company/$', views.create_company, name='create_company'),
    url(r'^oyunekle_finish/$', views.oyunekle_finish,name="oyunekle_finish"),
    url(r'^game_detail/(?P<game_name>\w+)$', views.generate_detail_html),
    url(r'^language_detector/$', views.language_detector,name="language_detector"),
    url(r'^game_form_search/$',views.games_detail_form,name="form_search"),

]
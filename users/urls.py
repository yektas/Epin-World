from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^auth_login/$', views.auth_login, name='auth_login'),

    #url(r'^loggedin/$', views.loggedin, name='loggedin'),
]
from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
]
from django.conf.urls import url

from users.views import userEntry, userAuth

app_name = 'users'

urlpatterns = [
    url(r'^profile/$', userEntry.profile, name='profile'),
    url(r'^register/$', userEntry.register, name='register'),
    url(r'^login/$', userEntry.login, name='login'),
    url(r'^logout/$', userEntry.logout, name='logout'),
    url(r'^auth_login/$', userAuth.auth_login, name='auth_login')
]

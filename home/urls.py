from django.conf.urls import url

from home import views

app_name = 'home'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^language_detector/$', views.language_detector, name='language_detector'),
]

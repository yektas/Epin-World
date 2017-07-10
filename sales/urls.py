from django.conf.urls import url
from sales import views

app_name = 'sales'

urlpatterns = [
    url(r'^checkout/$', views.checkout, name='checkout'),
]
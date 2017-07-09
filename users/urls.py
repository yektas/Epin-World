from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
    url(r'^profile/', views.profile,name= 'profile'),

]
from django.conf.urls import url

from sales import views

app_name = 'sales'

urlpatterns = [
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^addtocart/$', views.addtocart, name='addtocart'),
    url(r'^update_cart/$', views.update_cart, name='update_cart'),
    url(r'^deletecartitem/$', views.deletecartitem, name='deletecartitem'),
    url(r'^cart_json/$', views.cart_json, name='cart_json'),
]

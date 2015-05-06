from django.conf.urls import url
from orders import views

urlpatterns = [
    url(r'checkout', views.checkout, name='checkout'),
    url(r'finalize', views.finalize, name='finalize'),
    url(r'loaned', views.loaned, name='loaned'),
]

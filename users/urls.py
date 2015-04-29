from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'authenticate', views.authenticate),
    url(r'login', views.login),
    url(r'logout', views.logout),
]
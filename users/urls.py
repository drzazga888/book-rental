from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'authenticate', views.authenticate, name='authenticate'),
    url(r'login', views.login, name='login'),
    url(r'logout', views.logout, name='logout'),
    url(r'register', views.register, name='register'),
]

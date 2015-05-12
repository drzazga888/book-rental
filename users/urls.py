from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'authenticate', views.authenticate, name='authenticate'),
    url(r'login', views.login, name='login'),
    url(r'logout', views.logout, name='logout'),
    url(r'register', views.register, name='register'),
    url(r'confirm/user/(?P<user>[^/]+)/key/(?P<key>\w+)', views.confirm),
    url(r'remind', views.remind, name='remind'),
    url(r'reset/user/(?P<user>[^/]+)/key/(?P<key>\w+)', views.reset),
]

from django.conf.urls import include, url
from django.contrib import admin
from users import urls as users
from books import urls as books
from homepage import views as homepage

urlpatterns = [
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include(users)),
    url(r'^books/', include(books)),
    url(r'^index/', homepage.index),
    url(r'^$', homepage.index),
]

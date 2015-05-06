from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'book/(?P<book_id>[0-9]+)/comment', views.comment, name='comment'),
    url(r'book/(?P<book_id>[0-9]+)', views.book, name='book'),
    url(r'category/(?P<category>[0-9]+)', views.category, name='book'),
]

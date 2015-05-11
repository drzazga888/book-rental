from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'book/(?P<book_id>[0-9]+)/comment', views.comment, name='comment'),
    url(r'book/(?P<book_id>[0-9]+)', views.book, name='book'),
    url(r'category/(?P<cat>[0-9]+)/page/(?P<page>[0-9]+)', views.category, name='category'),
    url(r'category/(?P<cat>[0-9]+)', views.category_firstpage, name='category_firstpage'),
    url(r'perpage/(?P<length>[0-9]+)', views.perpage, name='perpage'),
]

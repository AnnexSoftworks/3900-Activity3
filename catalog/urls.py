from django.template.defaulttags import url
from django.urls import path, re_path

from locallibrary import settings
from . import views
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('author_detail/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

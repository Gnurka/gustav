from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authors/', views.AuthorListView.as_view(), name='author-list'), 
    url(r'^authors2/', views.authors2), 
]

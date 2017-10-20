from django.conf.urls import url
from . import views
from .models import Item

app_name = "forms"

urlpatterns = [
    url(r'^all/$', views.IndexView.as_view(), name='list'),
    url(r'all/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'item/add/$',views.ItemCreate.as_view(), name='item-create'),
    url(r'item/update/(?P<pk>[0-9]+)/$',views.ItemUpdate.as_view(), name='item-update'),
    url(r'item/update/$',views.ItemCreate.as_view(), name='item-update'),
    # url(r'item/(?P<pk>\d+)/update/$',views.ItemUpdate.as_view(), name='item-update'),
    url(r'item/(?P<pk>\d+)/delete/$',views.ItemDelete.as_view(), name='item-delete')
]

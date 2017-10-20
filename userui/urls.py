from django.conf.urls import url
from . import views

app_name = 'userui'

urlpatterns=[
    url(r'^all/$',views.index,name='index'),
]
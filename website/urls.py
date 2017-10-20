
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from forms.models import Item

from . import views

# app_name = "website"

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'accounts/',include('accounts.urls', namespace='accounts')),
    url(r'accounts/',include('django.contrib.auth.urls')),
    url(r'^userui/',include('userui.urls', namespace='userui')),
    url(r'^forms/',include('forms.urls', namespace='forms')),

    url(r'^test/$', views.TestPage.as_view(), name='test'),
    url(r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
##general--------------->
    url(r'test/pen/$', views.pen, name='pen'),
    url(r'test/pencils/$', views.pencil, name='pencil'),
    url(r'test/sim/$', views.sim, name='sim'),
    url(r'test/files/$', views.files, name='files'),
    url(r'test/sheets/$', views.sheets, name='sheets'),
    url(r'test/washing_powder/$', views.washing_powder, name='washing_powder'),
##genral completed---------------->

##HMC--------------->
    url(r'test/chess_boards/$', views.chess_boards, name='chess_boards'),
    url(r'test/tt_table/$', views.tt_table, name='tt_table'),
    url(r'test/cricket_bats/$', views.cricket_bats, name='cricket_bats'),
    url(r'test/cricket_balls/$', views.cricket_balls, name='cricket_balls'),
    url(r'test/footballs/$', views.footballs, name='footballs'),
    url(r'test/badminton/$', views.badminton, name='badminton'),
    url(r'test/washing_machine/$', views.washing_machine, name='washing_machine'),
##HMC completed------------------>

##Canteen----------------------->
    url(r'test/chips/$', views.chips, name='chips'),
    url(r'test/snacks/$', views.snacks, name='snacks'),
    url(r'test/biscuits/$', views.biscuits, name='biscuits'),
    url(r'test/beverages/$', views.beverages, name='beverages'),
##canteen completed--------------->

##Juice center---------------->
    url(r'test/amul_products/$', views.amul_products, name='amul_products'),
    url(r'test/fruits/$', views.fruits, name='fruits'),
    url(r'test/soft_drinks/$', views.soft_drinks, name='soft_drinks'),
    url(r'test/juice/$', views.juice, name='juice'),
##Juice center completed------------->
]

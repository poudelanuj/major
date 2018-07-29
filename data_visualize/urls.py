from django.conf.urls import url

from . import  views


urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^bubble',views.bubble,name='bubble'),
    url(r'^candle',views.candle,name='candle'),
    url(r'^line',views.line,name='line'),
    url(r'^cf',views.cf,name='cf'),
    url(r'^sentiment',views.sentiment,name='sentiment'),
    url(r'^sentiline',views.sentiline,name='sentiline'),
    url(r'^prediction',views.prediction,name='prediction'),
    url(r'^coin',views.coin,name='coin'),


]
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.Home.as_view(), name='Matrix'),
    url(r'Add', views.Entry.as_view(), name = 'Entry'),
    url(r'Orthagonalize', views.Orthagonalize, name = "Orthagonalize"),
    url(r'getEigens', views.getEigens, name = "getEigens"),
    url(r'RREF', views.RREF, name = "RREF"),
    url(r'Invert', views.Invert, name = "Invert"),
)
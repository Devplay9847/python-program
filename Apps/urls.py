from django.conf.urls import url
from . import views

app_name = "Apps"

urlpatterns = [
    url('r^$', views.home, name='home'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^login$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
 ]
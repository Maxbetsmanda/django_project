from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user_register', views.register),
    url(r'^user_login', views.login),
    url(r'^logout', views.logout)

]

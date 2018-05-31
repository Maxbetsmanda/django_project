from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^send$', views.home),
    url(r'^chat/(?P<user_id>\d+)$', views.chat)
]

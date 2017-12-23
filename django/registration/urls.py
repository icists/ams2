from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^applications/$', views.ApplicationList.as_view()),
    url(r'^applications/(?P<id>\d+)/$', views.ApplicationDetail.as_view()),
    url(r'^order/$', views.OrderDetail.as_view()),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^schools/$', views.SchoolList.as_view()),
    url(r'^profile/$', views.UserView.as_view()),
]

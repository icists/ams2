from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^schools/$', views.SchoolList.as_view()),
    url(r'^countries/$', views.CountryList.as_view()),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^stage/$', views.StageView.as_view()),
    url(r'^payment-info/$', views.PaymentInfoView.as_view()),
    url(r'^options/$', views.OptionList.as_view()),
    url(r'^accommodations/$', views.AccommodationOptionList.as_view()),
    url(r'^essay-topics/$', views.EssayTopicList.as_view()),
    url(r'^project-topics/$', views.ProjectTopicList.as_view()),
]

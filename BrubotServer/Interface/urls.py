from django.conf.urls import *
from . import views

app_name='Interface'

urlpatterns = [
    # urls for websites
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"newtask", views.NewTask.as_view(), name="newtask"),

    # urls for REST
    url(r"rest/claimTask", views.getWaitingOrStartedTasks, name="claimTask"),
    url(r"rest/getAllTasks", views.getAllTasks, name="getAllTasks"),
    url(r"rest/getWaitingTasks", views.getWaitingTasks, name="getWaitingTasks"),
    url(r"rest/getWaitingOrStartedTasks", views.getWaitingOrStartedTasks, name="getWaitingOrStartedTasks"),

    # urls for AJAX requests
    url(r"findTorrents", views.findTorrents, name="findTorrents"),
]

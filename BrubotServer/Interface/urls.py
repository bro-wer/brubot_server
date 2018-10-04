from django.conf.urls import *
from . import views

app_name='Interface'

urlpatterns = [
    # urls for websites
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"newtask", views.NewTask.as_view(), name="newtask"),

    # urls for AJAX requests
    url(r"findTorrents", views.findTorrents, name="findTorrents"),
]

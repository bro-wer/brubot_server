from django.conf.urls import *
from . import views

app_name='Interface'

urlpatterns = [
    # urls for websites
    # url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"getTasks", views.getTasks, name="getTasks"),
]

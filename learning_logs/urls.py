""" learning_logs-url"""

from django.conf.urls import url
from learning_logs import views
urlpatterns = [
    #main page
    url(r'^$', views.index, name = 'index'),
]
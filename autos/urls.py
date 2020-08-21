import os
from django.urls import include, path

from . import views

app_name="autos"
urlpatterns = [
    path('', view.MainView.as_view(), name="all"),
]


import os
from django.urls import include, path

import . from views

app_name="autos"
urlpatterns = [
    path('', view.MainView.as_view(), name="all"),
]


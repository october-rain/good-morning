from django.urls import path
from morningapp import api
urlpatterns = [
    path('morn-register/',api.morn_register),
    path('morn-login/',api.morn_login),
]
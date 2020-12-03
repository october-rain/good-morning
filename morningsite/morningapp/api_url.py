from django.urls import path
from morningapp import api
urlpatterns = [
    path('morn-register/',api.morn_register),
    path('morn-login/',api.morn_login),
    path('add-article/',api.add_article),
    path('get-articlelist/',api.get_articlelist),
    path('get-article/',api.get_article)
]
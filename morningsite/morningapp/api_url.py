from django.urls import path
from morningapp import api
urlpatterns = [
    path('morn-register/',api.morn_register),
    path('morn-login/',api.morn_login),
    path('change-password/',api.change_password),
    # 文章操作
    path('add-article/',api.add_article),
    path('get-articlelist/',api.get_articlelist),
    path('get-article/',api.get_article),
    path('del-article/',api.del_article),
    path('get-tag/',api.get_tag),


    # 获取个人信息
    path('get-message/',api.get_message),
    path('get-userarticle/',api.get_userarticle),
    # 获取标签下的文章
    path('get-taglist/',api.get_taglist)

    # path('test/',api.test)


]
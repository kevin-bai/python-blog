from django.urls import path, re_path
from . import views

urlpatterns = [
    path('index2/', views.index),  # 这是路由模式
    re_path(r'^index/$', views.index),  # 这是正则表达式模式
    re_path(r'^home/$', views.home)
]

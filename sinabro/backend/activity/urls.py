from django.shortcuts import render
from django.urls import path

from . import views

app_name = "activities"
urlpatterns = [
    path('', views.menu, name='menu_page'),
    path('select/', views.select, name='select_page'),
    path('do/', views.do, name='do_page'),
    path('write_action/', views.write_action, name='write_action_page'),
    path('post_list/', views.post_list, name='post_list_page'),
]


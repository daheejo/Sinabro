from django.shortcuts import render
from django.urls import path

from . import views

app_name = "chat"
urlpatterns = [
    path('', views.index, name='chat_page'),
    path('delete/', views.delete, name='delete_all_chat'),
    path('survey/', views.survey, name='survey_page'),
    path('survey_result/', views.survey_result, name='survey_result_page'),
    path('survey/delete/', views.survey_delete, name='delete_all_survey'),
]


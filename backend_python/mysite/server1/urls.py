# server1 > urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('memberInfo', views.memberInfo),
    path('predictTime', views.predictTime),
    path('Ingame', views.Ingame),
]

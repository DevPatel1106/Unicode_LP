from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('register/', views.registration, name='registerform'),
    path('login/', views.view_login, name='loginform'),
    path('mylists/', views.mylists, name='mylists'),
    path('listupdate/', views.listupdate, name='listupdate'),
    path('listadd/', views.listadd, name='listadd'),
    # path('listdelete/', views.listdelete, name='listdelete'),
    path('listdelete/<slug:title>', views.listdelete, name='listdelete'),
]

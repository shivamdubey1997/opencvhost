from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.startbutton,name="startbutton"),
    path('index',views.index,name="index"),


]
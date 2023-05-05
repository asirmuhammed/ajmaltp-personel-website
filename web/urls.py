from django.contrib import admin
from django.urls import path
from . import views

app_name="web"

urlpatterns = [
    path('', views.index,name="index"),
    path('profile',views.Profile,name="profile"),
    path('gallery',views.Gallery,name="gallery"),
    path('connect',views.Connect,name="connect")


]
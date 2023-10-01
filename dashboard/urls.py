from django.contrib import admin
from django.urls import path
from .views import dashboard, mascota

urlpatterns = [
    path('base/', dashboard, name="base"),
    path('mascota/', dashboard, name="mascota"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('data', views.data),  # Добавляем маршрут для /data
    path('test', views.test),  # Добавляем маршрут для /test
]

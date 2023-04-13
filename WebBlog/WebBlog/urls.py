from django.urls import path, re_path
from main import views

urlpatterns = [
    path('', views.authorization),
    re_path('main', views.main),
]
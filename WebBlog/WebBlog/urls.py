from django.urls import path, re_path,include
from main import views



urlpatterns = [
    path('', views.authorization),
    re_path('main/AdminPost',views.AdminPost),
    re_path("main/makePost", views.makePost),
    re_path('main/post',views.post),
    re_path('main', views.main),
   
]


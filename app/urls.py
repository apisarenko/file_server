from django.urls import path
from app import views


urlpatterns = [
    path('', views.file_list, name='file_list'),
    path('<str:date>/', views.file_list, name='file_list'),
    path('file/<str:name>/', views.file_content, name='file_content'),
]

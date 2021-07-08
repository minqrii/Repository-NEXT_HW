from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('new/', views.new, name="new"),
    path('detail/<int:post_pk>/', views.detail, name="detail"),
    path('edit/<int:post_pk>/', views.edit, name="edit"),
    path('delete/<int:post_pk>/', views.delete, name="delete"),
]
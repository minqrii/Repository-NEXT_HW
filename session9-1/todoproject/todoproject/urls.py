"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    #계정 관련
    path('registration/signup', views.signup, name="signup"),
    path('registration/login', views.login, name="login"),
    path('registration/logout', views.logout, name="logout"),
    path('accounts/', include('allauth.urls')),

    #서비스
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('mytodo', views.mytodo, name="mytodo"),
    path('new/', views.new, name="new"),
    path('detail/<int:todo_pk>', views.detail, name="detail"),
    path('delete/<int:todo_pk>', views.delete, name="delete"),
    path('delete_comment/<int:todo_pk>/<int:comment_pk>', views.delete_comment, name="delete_comment"),
    path('edit/<int:todo_pk>', views.edit, name="edit"),
]
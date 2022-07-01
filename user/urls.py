from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.SignUp.as_view(), name='register'),
    # path('admin/', views.account, name='admin'),
    path('admin/', admin.site.urls, name='admin')
]


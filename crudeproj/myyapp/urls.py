from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('create/', views.appointment_create, name='appointment_create'),
    path('<int:pk>/update/', views.appointment_update, name='appointment_update'),
    path('<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    path('appointment/set_reminder/<int:appointment_id>/create/', views.set_reminder_create, name='set_reminder_create'),
    path('set_reminder/list/<int:appointment_id>/', views.set_reminder_list, name='set_reminder_list'),
    path('save_reminder/', views.save_reminder, name='save_reminder'),
    path('set_reminder/<int:pk>/update/', views.set_reminder_update, name='set_reminder_update'),
    path('set_reminder/<int:pk>/delete/', views.set_reminder_delete, name='set_reminder_delete'),
]
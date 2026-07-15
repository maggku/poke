from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_display, name='tasks'),
    path('tasks/<int:email_id>/', views.email_detail, name='email_detail'),
]

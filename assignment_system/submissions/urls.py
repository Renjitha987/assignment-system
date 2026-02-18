from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name='assignment_list'),
    path('upload/<int:id>/', views.upload_assignment, name='upload'),
    path('register/', views.register, name='register'),
    path('my-submissions/', views.my_submissions, name='my_submissions'),
    path('register/', views.register, name='register'),


]

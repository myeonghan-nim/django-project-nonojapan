from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:no_id>/detail/', views.detail),

    path('new/', views.new),
    path('create/', views.create),
    
    path('<int:no_id>/edit/', views.edit),
    path('<int:no_id>/update/', views.update),
    
    path('<int:no_id>/delete/', views.delete),
]
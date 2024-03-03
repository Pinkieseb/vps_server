from django.urls import path
from . import views

urlpatterns = [
    path('add_reload/', views.add_reload, name='add_reload'),
    path('view_statistics/', views.view_statistics, name='view_statistics'),
]
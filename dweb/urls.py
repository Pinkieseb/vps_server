from django.urls import path
from . import views

urlpatterns = [
    path('add_order/', views.add_order, name='add_order'),
    path('add_tracking_number/', views.add_tracking_number, name='add_tracking_number'),
]
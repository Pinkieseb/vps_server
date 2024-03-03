from django.urls import path
from . import views

urlpatterns = [
    path('calc/', views.insulin_calculator, name='insulin_calculator'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('add_loss/', views.add_loss, name='add_loss'),
    path('list_losses/', views.list_losses, name='list_losses'),
]
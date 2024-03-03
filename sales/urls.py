from django.urls import path
from . import views
from .views import view_all_sales

urlpatterns = [
    path('add_sale/', views.add_sale, name='add_sale'),
    path('view-all-sales/', view_all_sales, name='view_all_sales'),
]
from django.urls import path
from .views import debt_manager_page, update_debt

urlpatterns = [
    path('debtmanager/', debt_manager_page, name='debt_manager_page'),
    path('debtmanager/update_debt/', update_debt, name='update_debt'),
]
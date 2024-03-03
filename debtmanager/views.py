from django.shortcuts import render
from .models import Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, DebtPayment

def debt_manager_page(request):
    customers = Customer.objects.all()
    print(f"Fetched {customers.count()} customers.")
    return render(request, 'debtmanager/debt_manager_page.html', {'customers': customers})

def update_debt(request):
    print("update_debt called")
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        action = request.POST.get('action')
        amount = float(request.POST.get('amount'))
        print(f"Updating debt for customer {customer_id}, action: {action}, amount: {amount}")
        customer = Customer.objects.get(id=customer_id)
        if action == 'increase':
            DebtPayment.objects.create(customer=customer, debt_increase=amount)
        elif action == 'decrease':
            DebtPayment.objects.create(customer=customer, debt_decrease=amount)
        print("Debt updated successfully")
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sale
from dweb.models import Order
from .forms import SaleForm
from django.http import JsonResponse
from django.shortcuts import render

def add_sale(request):
    print("add_sale called")
    if request.method == 'POST':
        print("POST request received")
        form = SaleForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            debt_change = form.cleaned_data.pop('debt_change', None)
            sale = form.save(commit=False)
            sale.save(debt_change=debt_change)
            print(f"Sale record added successfully: {sale.id}")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Sale record added successfully!'}, status=200)
            else:
                return HttpResponse('Sale record added successfully!')
    else:
        form = SaleForm()
    return render(request, 'sales/add_sale.html', {'form': form})

def view_all_sales(request):
    sales = Sale.objects.all()
    dweb_sales = Order.objects.all()  # Add this line to fetch dweb sales
    print(f"Number of sales fetched: {sales.count()}")
    return render(request, 'sales/view_all_sales.html', {'sales': sales, 'dweb_sales': dweb_sales})  # Update this line to include 'dweb_sales'
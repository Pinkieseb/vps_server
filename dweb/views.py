from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order
from .forms import OrderForm, TrackingNumberForm

def add_order(request):
    print("add_order called")
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            print(f"Order added successfully: {order.id}")
            return HttpResponse('Order added successfully!')
    else:
        form = OrderForm()
    return render(request, 'dweb/add_order.html', {'form': form})

def add_tracking_number(request):
    print("add_tracking_number called")
    if request.method == 'POST':
        form = TrackingNumberForm(request.POST)
        if form.is_valid():
            order = Order.objects.get(id=request.POST.get('order_id'))
            order.tracking_number = form.cleaned_data['tracking_number']
            order.save()
            print(f"Tracking number added to order: {order.id}")
            return redirect('add_tracking_number')
    else:
        orders = Order.objects.filter(tracking_number__isnull=True)
        forms = [TrackingNumberForm(initial={'order_id': order.id}) for order in orders]
    return render(request, 'dweb/add_tracking_number.html', {'forms': forms, 'orders': orders})

def view_dweb_sales(request):
    dweb_sales = Order.objects.all()
    name_filter = request.GET.get('dweb_name', None)
    order_id_filter = request.GET.get('order_id', None)

    if name_filter:
        dweb_sales = dweb_sales.filter(full_name__icontains=name_filter)
    if order_id_filter:
        dweb_sales = dweb_sales.filter(order_id__icontains=order_id_filter)

    return render(request, 'dweb/view_dweb_sales.html', {'dweb_sales': dweb_sales})
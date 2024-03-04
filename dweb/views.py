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
    # Filter orders to only those without a tracking number
    orders = Order.objects.filter(tracking_number__isnull=True)

    if request.method == 'POST':
        # Process the form submission
        form = TrackingNumberForm(request.POST)
        if form.is_valid():
            order_id = form.cleaned_data.get('order_id')
            tracking_number = form.cleaned_data.get('tracking_number')
            try:
                # Update the order with the tracking number
                order = orders.get(id=order_id)
                order.tracking_number = tracking_number
                order.save()
                print(f"Tracking number added to order: {order.id}")
                # Redirect to the same page to refresh the list of orders
                return redirect('add_tracking_number')
            except Order.DoesNotExist:
                print(f"Order with id {order_id} does not exist.")
        else:
            print("Form is not valid")
    else:
        # For GET requests, prepare a form for each order without a tracking number
        forms = [TrackingNumberForm(initial={'order_id': order.id}) for order in orders]

    # Pass the orders and their corresponding forms to the template
    orders_forms = zip(orders, forms)
    return render(request, 'dweb/add_tracking_number.html', {'orders_forms': orders_forms})

def view_dweb_sales(request):
    dweb_sales = Order.objects.all()
    name_filter = request.GET.get('dweb_name', None)
    order_id_filter = request.GET.get('order_id', None)

    if name_filter:
        dweb_sales = dweb_sales.filter(full_name__icontains=name_filter)
    if order_id_filter:
        dweb_sales = dweb_sales.filter(order_id__icontains=order_id_filter)

    return render(request, 'dweb/view_dweb_sales.html', {'dweb_sales': dweb_sales})
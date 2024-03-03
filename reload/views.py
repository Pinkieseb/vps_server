from django.shortcuts import render
from django.http import HttpResponse
from .models import Reload, Statistics
from .forms import ReloadForm
from django.utils import timezone
import datetime
from django.http import JsonResponse

def add_reload(request):
    print("add_reload called")
    if request.method == 'POST':
        form = ReloadForm(request.POST)
        if form.is_valid():
            reload = form.save()
            print(f"Reload record added successfully: {reload.id}")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Reload record added successfully!'}, status=200)
            else:
                return HttpResponse('Reload record added successfully!')
    else:
        form = ReloadForm()
    return render(request, 'reload/add_reload.html', {'form': form})

def view_statistics(request):
    stats, created = Statistics.objects.get_or_create(id=1)
    print(f"Statistics fetched: {stats.id}, created: {created}")
    return render(request, 'reload/view_statistics.html', {'stats': stats})

def view_statistics(request):
    stats, created = Statistics.objects.get_or_create(id=1)  # Ensure there's always a Statistics instance
    if stats.last_reload:
        # Calculate the difference between now and the last reload time
        now = timezone.now()
        time_difference = now - stats.last_reload

        # Convert the time difference to days, hours, minutes, and seconds
        days = time_difference.days
        seconds = time_difference.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 60)

        # Format the time difference
        formatted_time_difference = f"{days} Days, {hours} hours, {minutes} minutes, {seconds} seconds"

        # Pass the formatted time difference to the template instead of the raw last_reload time
        stats.last_reload_formatted = formatted_time_difference

    return render(request, 'reload/view_statistics.html', {'stats': stats})
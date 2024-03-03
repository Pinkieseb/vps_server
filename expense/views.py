from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Loss
from .forms import LossForm

def add_loss(request):
    print("add_loss called")
    if request.method == 'POST':
        print("POST request received for add_loss")
        form = LossForm(request.POST)
        if form.is_valid():
            print("Form is valid for add_loss")
            loss = form.save()
            print(f"Loss record added successfully: {loss.id}")
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Loss record added successfully!'}, status=200)
            else:
                return HttpResponse('Loss record added successfully!')
        else:
            print("Form is not valid for add_loss")
    else:
        form = LossForm()
    return render(request, 'expense/add_loss.html', {'form': form})

def list_losses(request):
    losses = Loss.objects.all()
    print(f"Number of losses fetched: {losses.count()}")
    return render(request, 'expense/list_losses.html', {'losses': losses})
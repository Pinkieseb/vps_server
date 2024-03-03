from django.shortcuts import render

def insulin_calculator(request):
    return render(request, 'insulinCalc/insulin_calculator.html')
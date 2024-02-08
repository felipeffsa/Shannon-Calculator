from django.shortcuts import render

# Create your views here.

def indice_calculator(request):
    return render(request,'interface/indice_calculator.html')

def digite_especies(request):
    return render(request,'interface/digite_especies.html')

def serve(request):
    return render(request,'interface/paraqueserve.html')

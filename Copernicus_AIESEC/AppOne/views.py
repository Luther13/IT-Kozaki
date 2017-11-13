from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'Copernicus_AIESEC/index.html')


def national_dashboard(request):
    return render(request, 'Copernicus_AIESEC/Nat-dash.html')
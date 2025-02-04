from django.shortcuts import render
from django.shortcuts import redirect
from .forms import StrainForm
from .serializers import StrainsSerializer
from django.http import JsonResponse
# Create your views here.

#now i have to answer to http request and send all the data with JSON

def strains(request):
    return render(request, 'strains.html')

def add_strain(request):
    if request.method == 'POST':
        form = StrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = StrainForm()
    return render(request, 'add_strain.html', {'form': form})
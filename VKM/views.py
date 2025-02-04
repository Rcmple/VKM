from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
# Create your views here.

#now i have to answer to http request and send all the data with JSON

def main_page(request):
    data = {
        'message': 'Семен дурак!'
    }
    return JsonResponse(data)
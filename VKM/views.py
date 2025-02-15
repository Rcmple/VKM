from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.middleware.csrf import get_token

def main_page(request):
    data = {
        'message': 'Семен!'
    }
    return JsonResponse(data)

def csrf_token_view(request):
    return JsonResponse({'csrfToken': get_token(request)})
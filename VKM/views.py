from django.http import JsonResponse

def main_page(request):
    data = {
        'message': 'Семен!'
    }
    return JsonResponse(data)
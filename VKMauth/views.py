from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            print(f"🔍 Получен запрос: {username} / {password}")

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'message': 'Вход выполнен', 'user': user.username})
            else:
                return JsonResponse({'error': 'Неверные данные'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Ошибка в JSON формате'}, status=400)

    return JsonResponse({'error': 'Требуется POST-запрос'}, status=400)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"message": "Вы успешно вышли"}, status=200)
    return JsonResponse({"error": "Только POST-запрос разрешен"}, status=400)


def auth_status_view(request):
    if request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': True, 'username': request.user.username})
    return JsonResponse({'isAuthenticated': False})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'message': 'Вход выполнен', 'user': user.username})
        else:
            return JsonResponse({'error': 'Неверные данные'}, status=400)
    return JsonResponse({'error': 'Требуется POST-запрос'}, status=400)

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Пользователь уже существует'}, status=400)
        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # Сразу входим после регистрации
        return JsonResponse({'message': 'Регистрация успешна', 'user': user.username})
    return JsonResponse({'error': 'Требуется POST-запрос'}, status=400)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Выход выполнен'})

def user_status(request):
    if request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': True, 'user': request.user.username})
    return JsonResponse({'isAuthenticated': False})

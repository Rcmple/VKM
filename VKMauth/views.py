from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, LoginSerializer, AddUserSerializer
from .permissions import IsModerator
from django.contrib.auth.models import User


class AuthStatusView(APIView):

    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"isAuthenticated": False, "user": None})
        else:
            user = User.objects.get(username=user.username)
            user_data = UserSerializer(user).data
            return Response({"isAuthenticated": True, "user": user_data})


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        if request.user.is_authenticated:
            return Response({
                'error': {
                    'ru': 'Вы уже авторизованы',
                    'en': 'You are already authorized'
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)

                user_serializer = UserSerializer(user)
                user_data = user_serializer.data
                refresh = RefreshToken.for_user(user)

                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'user': user_data,
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': {
                        'ru': 'Пользователь не найден, возможно вы ввели неверный логин или пароль',
                        'en': 'User not found, maybe you entered an incorrect username or password.'
                    }
                },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': {
            'ru': 'Вы вышли из системы',
            'en': 'You have logged out'
        }}, status=status.HTTP_200_OK)


class AddUserView(APIView):
    permission_classes = [IsModerator]

    def post(self, request):
        serializer = AddUserSerializer(data=request.data)
        if serializer.is_valid():
            is_moder = serializer.validated_data.pop('isModerator')
            user = serializer.save()
            if is_moder:
                user.groups.add('Moderator')

            return Response({"message": {
                "ru": "Пользователь успешно зарегистрирован",
                "en": "User successfully registered"
            }},
                status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUserView(APIView):
    permission_classes = [IsModerator]

    def delete(self, request):
        user = User.objects.get(id=request.data.get('user_id'))
        if user:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({
                'error': {
                    'ru': 'Пользователь не найден',
                    'en': 'User not found'
                }
            }, status=status.HTTP_400_BAD_REQUEST)


class UsersListView(APIView):
    permission_classes = [IsModerator]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class ChangeUserPasswordView(APIView):
    permission_classes = [IsModerator]

    def post(self, request):
        user = User.objects.get(username=request.data.get('user').get('username'))
        if user:
            user.set_password(request.data.get('user').get('new_password'))
            user.save()
            return Response({"message":{
                "ru": "Пароль успешно изменен",
                "en": "Password successfully changed"
            }}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({
                'error': {
                    'ru': 'Пользователь не найден',
                    'en': 'User not found'
                }
            }, status=status.HTTP_400_BAD_REQUEST)

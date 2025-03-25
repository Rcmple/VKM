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
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.groups.filter(name='Moderator').exists():
            return Response({"isAuthenticated": True, "username": request.user.username, "isModerator": True})
        return Response({"isAuthenticated": True, "username": request.user.username, "isModerator": False})
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
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)

                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'user': UserSerializer(user).data
                })
            else:
                return Response({
                        'error':{
                            'ru':'Пользователь не найден, возможно вы ввели неверный логин или пароль',
                            'en':'User not found, maybe you entered an incorrect username or password.'
                        }
                    },
                    status = status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersListView(APIView):
    permission_classes = [IsModerator]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class AddUserView(APIView):
    permission_classes = [IsModerator]

    def post(self, request):
        serializer = AddUserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                email=serializer.validated_data.get('email')
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": {
                'ru' : "Вы успешно вышли",
                'en' : "You have successfully logged out"
            }
        }, status=status.HTTP_200_OK)
class DeleteUserView(APIView):
    permission_classes = [IsModerator]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(username=serializer.validated_data['username'])
                user.delete()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({
                    'error': {
                        'ru': 'Пользователь не найден',
                        'en': 'User not found'
                    }
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
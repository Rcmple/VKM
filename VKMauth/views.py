from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, LoginSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample


class LoginView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(
                response=UserSerializer,
                description="Успешный вход. Возвращает токены и информацию о пользователе.",
                examples=[
                    OpenApiExample(
                        name="Successful Login",
                        value={
                            "access": "access_token_example",
                            "refresh": "refresh_token_example",
                            "user": {"id": 1, "username": "test_user", "email": "test@example.com"}
                        }
                    )
                ]
            ),
            400: OpenApiResponse(
                description="Ошибка аутентификации или валидации запроса.",
                examples=[
                    OpenApiExample(
                        name="Invalid Credentials",
                        value={
                            "error": {
                                "ru": "Пользователь не найден, возможно вы ввели неверный логин или пароль",
                                "en": "User not found, maybe you entered an incorrect username or password."
                            }
                        },
                    ),
                    OpenApiExample(
                        name="Validation Error - Missing Fields",
                        value={
                            "username": ["Обязательное поле."],
                            "password": ["Обязательное поле."]
                        },
                    ),
                    OpenApiExample(
                        name="Validation Error - Incorrect Format",
                        value={
                            "username": ["Введите корректный email."],
                            "password": ["Длина пароля должна быть не менее 8 символов."]
                        },
                    ),
                ]
            ),
        }
    )
    def post(self, request):
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

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Вы успешно вышли"}, status=status.HTTP_200_OK)


class AuthStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"isAuthenticated": True, "username": request.user.username})
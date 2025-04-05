## 2. VKMAuth (Аутентификация)
### Эндпоинты:
- **`[POST] /api/auth/login/`** – Авторизация пользователя.

  - **Описание:** Этот эндпоинт используется для входа пользователя в систему. Если пользователь уже авторизован, возвращается ошибка.
  - **Тело запроса(POST):**
    ```json
    {
      "username": "string",
      "password": "string"
    }
    ```
  - **Ответ (успешный вход, HTTP_200_OK):**
    ```json
    {
      "access": "access_token",
      "refresh": "refresh_token",
      "user": {
        "id": 1,
        "username": "user123",
        "email": "user@example.com",
        "first_name": "Имя",
        "last_name": "Фамилия",
        "date_joined": "2024-04-04T12:34:56Z",
        "isModerator": false
      }
    }
    ```
  - **Ответ (ошибка аутентификации, HTTP_400_BAD_REQUEST):**
    ```json
    {
      "error": {
        "ru": "Пользователь не найден, возможно вы ввели неверный логин или пароль",
        "en": "User not found, maybe you entered an incorrect username or password."
      }
    }
    ```
  - **Ответ (если пользователь уже авторизован, HTTP_400_BAD_REQUEST):**
    ```json
    {
      "error": {
        "ru": "Вы уже авторизованы",
        "en": "You are already authorized"
      }
    }
    ```
- **`[POST] /api/auth/logout/`** – Выход пользователя из системы.

  - **Описание:** Этот эндпоинт используется для выхода авторизованного пользователя из системы. Требует аутентификации.
  - **Ответ (успешный выход, HTTP_200_OK):**
    ```json
    {
      "message": {
        "ru": "Вы вышли из системы",
        "en": "You have logged out"
      }
    }
    ```
    
  - **Ответ (Попытка выхода без аутентификации, HTTP_400_BAD_REQUEST):**
      ```json
      {
        "detail": "You do not have permission to perform this action."
      }
      ```
- **`[GET] /api/auth/status/`** – Проверка статуса аутентификации пользователя.

  - **Описание:** Этот эндпоинт используется для проверки, авторизован ли пользователь в системе.
  - **Ответ (пользователь не аутентифицирован, HTTP_200_OK):**
    ```json
    {
      "isAuthenticated": false,
      "user": null
    }
    ```
  - **Ответ (пользователь аутентифицирован, HTTP_200_OK):**
    ```json
    {
      "isAuthenticated": true,
      "user": {
        "id": 1,
        "username": "user123",
        "email": "user@example.com",
        "first_name": "Имя",
        "last_name": "Фамилия",
        "date_joined": "2024-04-04T12:34:56Z",
        "isModerator": false
      }
    }
    ```
- **`[POST] /api/auth/token/refresh/`** – Обновление JWT-токена.

  - **Описание:** Этот эндпоинт используется для обновления истекшего access-токена с помощью refresh-токена.
  - **Тело запроса:**
    ```json
    {
      "refresh": "refresh_token"
    }
    ```
  - **Ответ (успешное обновление токена):**
    ```json
    {
      "access": "new_access_token"
    }
    ```
  - **Ответ (ошибка, например, истекший или недействительный refresh-токен):**
    ```json
    {
      "detail": "Token is invalid or expired"
    }
    ```
- **`[POST] /api/auth/add_user/`** – Регистрация нового пользователя.

  - **Описание:** Этот эндпоинт используется для регистрации нового пользователя в системе.
  - **Тело запроса:**
    ```json
     {
      "user": {
        "username": "string",
        "password": "string",
        "email": "string",
        "first_name": "string",
        "last_name": "string",
        "isModerator": false
      }
    }
    ```
  - **Ответ (успешная регистрация, HTTP_201_CREATED):**
    ```json
    {
      "message": {
        "ru": "Пользователь успешно зарегистрирован",
        "en": "User successfully registered"
      }
    }
    ```
  - **Ответ (ошибка, например, пользователь уже существует, HTTP_400_BAD_REQUEST):**
    ```json
    {
      "error": {
        "ru": "Пользователь с таким именем уже существует",
        "en": "A user with this name already exists"
      }
    }
    ```
- **`[DELETE] /api/auth/delete_user/`** – Удаление пользователя.

  - **Описание:** Этот эндпоинт используется для удаления пользователя из системы. Требует роль модератора.
  - **Тело запроса:**
    ```json
    {
      "user_id": 1
    }
    ```
  - **Ответ (успешное удаление, HTTP_204_NO_CONTENT):**
    ```json
    {
      "message": {
        "ru": "Пользователь успешно удален",
        "en": "User successfully deleted"
      }
    }
    ```
  - **Ответ (ошибка, например, пользователь не найден, HTTP_400_BAD_REQUEST):**
    ```json
    {
      "error": {
        "ru": "Пользователь не найден",
        "en": "User not found"
      }
    }
    ```
- **`[GET] /api/auth/users_list/`** – Список зарегистрированных юзеров.

  - **Описание:** Этот эндпоинт используется для получения списка всех зарегистрированных пользователей. Требует роль модератора.
  - **Ответ (Успешный возраст списка всех пользователей коллекции, HTTP_200_OK):**
    ```json
    [
      {
        "id": 1,
        "username": "user123",
        "email": "user@example.com",
        "first_name": "Имя",
        "last_name": "Фамилия",
        "date_joined": "2025-04-04T12:34:56Z",
        "isModerator": false
      },
      
      {
        "id": 2,
        "username": "user123",
        "email": "user@example.com",
        "first_name": "Имя",
        "last_name": "Фамилия",
        "date_joined": "2024-03-04T12:34:56Z",
        "isModerator": true
      }
    ]
    ```
  - **Ответ (ошибка, например, недостаточно прав, HTTP_403_FORBIDDEN):**
      ```json
      {
      "detail": "You do not have permission to perform this action."
      }
      ```
    
- **`[POST] /api/auth/change_user_password/`** – Изменение пароля пользователя.

  - **Описание:** Этот эндпоинт используется для изменения пароля пользователя. Требует роль модератора.
  - **Тело запроса:**
    ```json
    {
      "user": {
        "id": 1,
        "username": "string",
        "new_password": "string",
      }
    }
    ```
  - **Ответ (успешное изменение пароля, HTTP_204_NO_CONTENT):**
    ```json
    {
      "message": {
        "ru": "Пароль успешно изменен",
        "en": "Password successfully changed"
      }
    }
    ```
  - **Ответ (Пользователь не найден, HTTP_400_BAD_REQUEST):**
    ```json
    {
      "error": {
        "ru": "Пользователь не найден",
        "en": "User not found"
      }
    }
    ```
  - **Ответ (Недостаточно прав, HTTP_403_FORBIDDEN):**
    ```json
    {
      "detail": "You do not have permission to perform this action."
    }
    ```


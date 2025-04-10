## 4. Search (Поиск)
### **`[GET] /api/strains/search/`** – *Поиск штаммов по названию рода (Genus) и виду (Species)*

- **Описание:**  
  Этот эндпоинт позволяет выполнять полнотекстовый поиск штаммов по полям `Strain`, `Genus` и `Species` с использованием триграммного сравнения. Запрос может содержать несколько слов (разделённых пробелами), и будет выполнен приблизительный поиск по каждому слову. Результаты сортируются по степени схожести.

- **Параметры запроса:**
  - `q` (обязательный) – поисковая строка (может содержать одно или несколько слов).
  - `offset` (необязательный, по умолчанию 0) – Начальная позиция для пагинации.
  - `limit` (необязательный, по умолчанию 100) – Количество результатов на странице.

- **Ответ (успешный запрос, HTTP_200_OK):**
```json
      {
        "count": 100,
        "next": "string",
        "previous": "string",
        "results": [
          {
            "strain_id": 1,
            "CollectionCode": "string",
            "Strain": "string",
            "Genus": "string",
            "Species": "string",
            "Variant": "string",
            "AuthoritySp": "string",
            "TypeOfSubstrate": {
              "en": "string",
              "ru": "string"
            },
            "Country": {
              "en": "string",
              "ru": "string"
            },
            "IsolationDate": "string"
          }
          
            // ... другие штаммы
        ]
      }
```

- **Ответ (ошибка – отсутствует параметр `q`, HTTP_400_BAD_REQUEST):**
  ```json
  {
    "error": {
      "ru": "Параметр q не найден",
      "en": "Parameter q not found"
    }
  }
  ```

- **Ответ (ошибка – пустой или некорректный запрос, HTTP_400_BAD_REQUEST):**
  ```json
  {
    "error": "Введите корректный запрос"
  }
  ```


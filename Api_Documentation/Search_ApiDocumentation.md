
## 4. Search (Поиск)

### **`[POST] /api/strains/search/`** – *Расширенный поиск штаммов по различным полям*

- **Описание:**  
  Этот эндпоинт позволяет выполнять гибкий и точный поиск штаммов по следующим полям:

  - `Strain` — номер штамма
  - `TaxonName` — полнотекстовый поиск по таксономическому названию
  - `StatusOfStrain` — фильтрация по статусу штамма
  - `OtherCol` — поиск по другим коллекциям
  - `IsolatedFrom` — полнотекстовый поиск по источнику выделения
  - `Geographics` — полнотекстовый поиск по географическим данным
  - `Country` — полнотекстовый поиск по стране
  - `Any` — полнотекстовый поиск по всем полям

- **Формат запроса:**

  ```json
  {
    "query": {
      "Strain": "5075",
      "TaxonName": "Sarcopodium vanillae",
      "StatusOfStrain": "type",
      "OtherCol": "CBS 12345",
      "IsolatedFrom": "forest litter",
      "Geographics": "southern Vietnam",
      "Country": "Vietnam",
      "Any": "vanillae Vietnam forest"
    }
  }
  ```

- **Параметры пагинации (в query-параметрах URL):**
  - `offset` – начальная позиция (по умолчанию 0)
  - `limit` – количество результатов (по умолчанию 100)

- **Ответ (успешный запрос, HTTP 200 OK):**
  ```json
  {
    "count": 100,
    "next": "http://example.com/api/strains/search/?offset=100&limit=100",
    "previous": null,
    "results": [
      {
        "strain_id": 41867,
        "VKM_number": {
          "CollectionCode": "VKM",
          "Subcollection": "F",
          "Strain": 5075.0
        },
        "Genus": "Sarcopodium",
        "Species": "vanillae",
        "Variant": "",
        "AuthoritySp": "(Petch) B. Sutton 1981",
        "TypeOfSubstrate": {
          "en": "plant detritus",
          "ru": "растительные остатки"
        },
        "Country": {
          "en": "Vietnam",
          "ru": "Вьетнам"
        },
        "IsolationDate": "2022-07-12"
      }
    ]
  }
  ```

- **Ответ (ошибка – отсутствует поле `query`, HTTP 400 BAD REQUEST):**
  ```json
  {
    "error": {
      "en": "Query parameter is required",
      "ru": "Параметр запроса обязателен"
    }
  }
  ```


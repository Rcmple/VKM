
## 4. Search (Поиск)

### **`[GET] /api/strains/search/`** – *Расширенный поиск штаммов по различным полям*

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
  Параметры передаются в строке запроса URL следующим образом(Каких-то полей может и не быть):

  ```
  /api/strains/search/?Strain=some_strain&TaxonName=some_taxon_name&StatusOfStrain=some_status&OtherCol=some_value&IsolatedFrom=some_location&Geographics=some_geographics&Country=some_country&Any=some_query
  ```
  Также перед параметрами и знаком '?' может отсутствовать '/'

  ```
  /api/strains/search?Strain=some_strain&TaxonName=some_taxon_name&StatusOfStrain=some_status&OtherCol=some_value&IsolatedFrom=some_location&Geographics=some_geographics&Country=some_country&Any=some_query
  ```
  
- 
  Пример запроса:

  ```
  /api/strains/search/?Strain=5075&TaxonName=Sarcopodium%20vanillae&StatusOfStrain=type&OtherCol=CBS%2012345&IsolatedFrom=forest%20litter&Geographics=southern%20Vietnam&Country=Vietnam&Any=vanillae%20Vietnam%20forest
  ```

- **Параметры пагинации (в query-параметрах URL):**
  - `offset` – начальная позиция (по умолчанию 0)
  - `limit` – количество результатов (по умолчанию 100)

  Пример с пагинацией:

  ```
  /api/strains/search/?Strain=5075&TaxonName=Sarcopodium%20vanillae&offset=0&limit=50
  ```

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
  
      // ... другие результаты
    ]
  }
  ```

- **Ответ (ошибка – отсутствует обязательный параметр, HTTP 400 BAD REQUEST):**
  ```json
  {
    "error": {
      "en": "Query parameter is required",
      "ru": "Параметр запроса обязателен"
    }
  }
  ```

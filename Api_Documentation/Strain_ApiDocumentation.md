## 3. Strains (Штаммы)

### Эндпоинты:

- **`[GET] /api/strains/get_strains/`** – *Получение списка всех штаммов.*
    - **Описание:** Этот эндпоинт используется для получения списка всех штаммов. Можно использовать параметры `offset`
      и `limit` для пагинации.
    - **Параметры:**
        - `offset` (по умолчанию 0) – Начальная позиция для выборки.
        - `limit` (по умолчанию 100) – Максимальное количество записей для выборки.
    - **Ответ (успешный запрос, HTTP_200_OK):**
    - ```json
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
- **`[GET] /api/strains/get_changed_strains/`** – *Получение списка измененных штаммов.*
    - **Описание:** Этот эндпоинт используется для получения списка измененных штаммов. Можно использовать
      параметры `offset` и `limit` для пагинации.
    - **Параметры:**
        - `offset` (по умолчанию 0) – Начальная позиция для выборки.
        - `limit` (по умолчанию 100) – Максимальное количество записей для выборки.
    - **Ответ (успешный запрос, HTTP_200_OK):**
    - ```json
      {
        "count": 100,
        "next": "string",
        "previous": "string",
        "results": [
          {
            "strain": {
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
            },
            "changed_by": {
                "id": 1,
                "username": "string",
                "email": "string",
                "first_name": "string",
                "last_name": "string",
                "date_joined": "string",
                "isModerator": false
            },
            "changes": {
                "field_name": "type_of_field_name",
                "field_name2": "type_of_field_name2"
                //и так далее
            },
            "created_at": "string",
            "updated_at": "string",
            "approved": false
          }
          
            // ... другие штаммы
        ]
      }
      ```
    - **Ответ (ошибка, например, недостаточно прав, HTTP_403_FORBIDDEN):**
      ```json
      {
        "detail": "You do not have permission to perform this action."
      }
      ```
- **`[GET] /api/strains/get_new_strains/`** – *Получение списка новых штаммов.*
    - **Описание:** Этот эндпоинт используется для получения списка новых штаммов. Можно использовать параметры `offset`
      и `limit` для пагинации.
    - **Параметры:**
        - `offset` (по умолчанию 0) – Начальная позиция для выборки.
        - `limit` (по умолчанию 100) – Максимальное количество записей для выборки.
    - **Ответ (успешный запрос, HTTP_200_OK):**
    - ```json
      {
        "count": 100,
        "next": "string",
        "previous": "string",
        "results": [
          {
            "created_by": {
                "id": 1,
                "username": "string",
                "email": "string",
                "first_name": "string",
                "last_name": "string",
                "date_joined": "string",
                "isModerator": false
            },
            "changes": {
                "field_name": "type_of_field_name",
                "field_name2": "type_of_field_name2"
                //и так далее
            },
            "created_at": "string",
            "updated_at": "string",
            "approved": false
          
            // ... другие штаммы
          }
        ]
      }
      ```
    - **Ответ (ошибка, например, недостаточно прав, HTTP_403_FORBIDDEN):**
      ```json
      {
        "detail": "You do not have permission to perform this action."
      }
      ```
- **`[GET] /api/strains/{strain_id}/`** – *Получение информации о конкретном штамме.*
    - **Описание:** Этот эндпоинт используется для получения информации о конкретном штамме по его ID.
    - **Параметры:**
        - `strain_id` – ID штамма, информацию о котором нужно получить.
    - **Ответ (успешный запрос, HTTP_200_OK):**
    - ```json
      {
        "strain_id": 1,
        "NameAndTaxonomy": {
          "CollectionCode": "string",
          "Subcollection": "string",
          "Genus": "string",
          "Species": "string",
          "Variant": "string",
          "Forma": "string",
          "FormaSpecies": "string",
          "Strain": "string",
          "AuthoritySp": "string",
          "AuthoritySubSp": "string",
          "Family": "string",
          "Order": "string",
          "Class": "string",
          "Synonym": "string",
          "TaxonomicID": "string",
          "Current_Name_DSMZ_MycoBank": "string",
          "Link_to_TaxonomicID": "string",
          "Pathogenicgroup": "string",
          "Risk_group": "string",
          "SanPin": "string",
          "State": "string",
          "Type": {
            "en": "string",
            "ru": "string"
          },
          "Qouts": "string",
          "OtherName": "string",
          "ClassShort": "string",
          "References": "string",
          "References_ncbi": "string",
          "Race": "string",
          "Serovar": "string",
          "OtherCol": "string"
        },
        "History": {
          "ReceivedFrom": {
            "en": "string",
            "ru": "string"
          },
          "Depositor": {
            "en": "string",
            "ru": "string"
          },
          "ReceivedAs": "string",
          "ReceivedDate": "2024-04-04",
          "AccessionDate": "2024-04-05",
          "TypeOfSubstrate": {
            "en": "string",
            "ru": "string"
          },
          "IsolatedFrom": {
            "en": "string",
            "ru": "string"
          },
          "AnatomicPart": {
            "en": "string",
            "ru": "string"
          },
          "Location": {
            "en": "string",
            "ru": "string"
          },
          "Geographics": {
            "en": "string",
            "ru": "string"
          },
          "Country": {
            "en": "string",
            "ru": "string"
          },
          "USSR": "string",
          "CollectedBy": {
            "en": "string",
            "ru": "string"
          },
          "CollectedDate": "2024-04-06",
          "IsolationDate": "2024-04-07",
          "IsolatedBy": {
            "en": "string",
            "ru": "string"
          },
          "IsolateNumber": {
            "en": "string",
            "ru": "string"
          },
          "IdentificateBy": {
            "en": "string",
            "ru": "string"
          },
          "IdentificateDate": "2024-04-08"
        },
        "CultivationAndStorage": {
          "IncubationTemp": "string",
          "Tested_temperature_growth_range": "string",
          "GrowthMedium": "string",
          "GrowthCondition": {
            "en": "string",
            "ru": "string"
          },
          "StorageMethods": "string",
          "StorageFreeze": "string",
          "StorageOil": "string",
          "StorageSilicagel": "string",
          "StorageWater": "string",
          "StorageNitrogen": "string",
          "StorageSubcultivation": "string",
          "StorageSoil": "string"
        },
        "StrainCharacteristics": {
          "EnzymeProduction": {
            "en": "string",
            "ru": "string"
          },
          "MetaboliteProduction": {
            "en": "string",
            "ru": "string"
          },
          "Transformation": {
            "en": "string",
            "ru": "string"
          },
          "Degradation": {
            "en": "string",
            "ru": "string"
          },
          "Other": {
            "en": "string",
            "ru": "string"
          },
          "MatingType": "string",
          "DNA_Sequence_Accession_Numbers": "string"
        },
        "GeneralInformation": {
          "Latitude": "string",
          "Longitude": "string",
          "Altitude": "string",
          "Curator": "string",
          "Category": "string",
          "Restrictions_on_use": "string",
          "Remarks": "string",
          "EntryDate": "2024-04-09",
          "EditDate": "2024-04-10",
          "Reidentif": {
            "en": "string",
            "ru": "string"
          },
          "Confidential_Information": "string",
          "Application": {
            "en": "string",
            "ru": "string"
          },
          "Form_of_supply": "string",
          "Report2020": "string",
          "Report2021": "string"
        }
      }
        ```

    - **Ответ (ошибка, например, штамм не найден, HTTP_404_NOT_FOUND):**
        ```json
        {
            "error": {
                "ru": "Штамм не найден",
                "en": "Strain not found"
            }
        }
        ```

- **`[POST] /api/strains/{strain_id}/edit/`** – *Редактирование информации о штамме.*
    - **Описание:** Этот эндпоинт используется для редактирования информации о конкретном штамме по его ID.
    - **Параметры:**
        - `strain_id` – ID штамма, информацию о котором нужно редактировать.
    - **Тело запроса(POST):**
        ```json
        {
             "changes": {
              "field_name": "value",
              "field_name2": "value2"
              // и так далее
            }
        }
        ```
    - **Ответ (успешный запрос, HTTP_201_CREATED):**
    -  **Ответ (Невалидные данные, например, неверный формат даты, HTTP_400_BAD_REQUEST):**
        ```json
        {
            "error": {
                "ru": "Некорректные данные",
                "en": "Invalid data"
            }
        }
        ```
- **`[PUT] /api/strains/{strain_id}/edit/`** – *Редактирование информации о штамме.*
    - **Описание:** Этот эндпоинт используется для одобрения редактирования информации о конкретном штамме по его ID.
    - **Параметры:**
        - `strain_id` – ID штамма, информацию о котором нужно редактировать.
    - **Тело запроса(PUT):**
        ```json
        {
            "change_request_id": 1
            // и так далее
        }
        ```
    - **Ответ (успешный запрос, HTTP_200_OK):**
        ```json
        {
            "message": {
                "ru": "Запрос на изменение одобрен и изменения применены к StrainModel",
                "en": "Change request approved and changes applied to StrainModel"
            }
        }
        ```
    -  **Ответ (change_request_id не найден, HTTP_404_NOT_FOUND):**
        ```json
        {
            "error": {
                "ru": "Запрос на изменение не найден или не принадлежит данному штамму",
                "en": "Change request not found or does not belong to this strain"
            }
        }
        ```
    - **Ответ (ошибка, например, недостаточно прав, HTTP_403_FORBIDDEN):**
        ```json
        {
            "detail": "You do not have permission to perform this action."
        }
        ```
    - **Ответ (Этот запрос на изменения уже был одобрен, HTTP_400_BAD_REQUEST):**
        ```json
        {
            "error": {
                "ru": "Этот запрос на изменения уже был одобрен",
                "en": "This change request has already been approved"
            }
        }
        ```

- **`[POST] /api/strains/add/`** – *Добавление нового штамма.*
    - **Описание:** Этот эндпоинт используется для добавления нового штамма в систему.
    - **Тело запроса(POST):**
        ```json
        {
            "changes": {
              "field_name": "value",
              "field_name2": "value2"
              // и так далее,
            }
        }
        ```
    - **Ответ (успешный запрос, HTTP_201_CREATED):**
    -  **Ответ (ошибка, например, недостаточно прав, HTTP_403_FORBIDDEN):**
        ```json
        {
            "detail": "You do not have permission to perform this action."
        }
        ```
    - **Ответ (невалидные данные, например, неверный формат даты, HTTP_400_BAD_REQUEST):**

- **`[PUT] /api/strains/add/`** – *Добавление нового штамма.*
    - **Описание:** Этот эндпоинт используется для одобрения добавления нового штамма в систему.
    - **Тело запроса(PUT):**
        ```json
        {
            "new_request_id": 1
            // и так далее
        }
        ```
    - **Ответ (успешный запрос, HTTP_200_OK):**
        ```json
        {
            "message": {
                "ru": "Запрос на добавление одобрен и новый штамм добавлен в StrainModel",
                "en": "Add request approved and new strain added to StrainModel"
            }
        }
        ```
    -  **Ответ (change_request_id не найден, HTTP_404_NOT_FOUND):**
        ```json
        {
            "error": {
                "ru": "Запрос на добавление не найден или не принадлежит данному штамму",
                "en": "Add request not found or does not belong to this strain"
            }
        }
        ```
    - **Ответ (ошибка, например, недостаточно прав, HTTP_403_FORBIDDEN):**
        ```json
        {
            "detail": "You do not have permission to perform this action."
        }
        ```
    - **Ответ (Запрос уже был одобрен, HTTP_400_BAD_REQUEST):**
        ```json
        {
            "error": {
                "ru": "Этот запрос на добавление уже был одобрен",
                "en": "This add request has already been approved"
            }
        }
        ```

- **`[POST] /api/strains/upload/`** – *Загрузка файла с данными о штаммах.*
    - **Описание:** Этот эндпоинт используется для загрузки файла с данными о штаммах в формате CSV.
    - **Тело запроса(POST):**
        ```json
        {
            "file": "file.csv"
        }
        ```
    - **Ответ (успешный запрос, HTTP_201_CREATED):**
    -  **Ответ (ошибка, например, недостаточно прав, HTTP_403_FORBIDDEN):**
        ```json
        {
            "detail": "You do not have permission to perform this action."
        }
        ```
    - **Ответ (невалидные данные, например, неверный формат файла, HTTP_400_BAD_REQUEST):**
        ```json
        {
            "error": {
                "ru": "Некорректные данные в файле",
                "en": "Invalid data in file"
            }
        }
        ```

## 3. Strains (Штаммы)

### Эндпоинты:
#### Эндпоинты связанные с получением списка:
- **`[GET] /api/strains/{strain_id_param}/`** – *Получение информации о конкретном штамме.*
    - **Описание:** Этот эндпоинт используется для получения информации о конкретном штамме по его ID.
    - **Параметры:**
        - `strain_id` – ID штамма, информацию о котором нужно получить.
    - **Ответ (успешный запрос для неавторизованного пользователя, HTTP_200_OK):**
      - ```json
        {
            "strain_id": 4,
            "NameAndTaxonomy": {
                "VKM_number": {
                    "CollectionCode": "VKM",
                    "Subcollection": "F",
                    "Strain": 5048
                },
                "Genus": "Penicillium",
                "Species": "scabrosum",
                "Variant": null,
                "AuthoritySp": "Frisvad, Samson et Stolk 1990",
                "Family": "Aspergillaceae",
                "Order": "Eurotiales",
                "Class": "Eurotiomycetes",
                "TaxonomicID": 136735,
                "CurrentName": null,
                "Link_to_TaxonomicID": "https://www.mycobank.org/page/Name%20details%20page/field/Mycobank%20%23/136735",
                "Pathogenicgroup": "4",
                "RiskGroup": "no",
                "SanPin": "Данный штамм относится к виду, который включен в 4-ую группу патогенности по СанПиН 3.3686-21, утв. Постановлением Главного государственного санитарного врача РФ от 28.01.2021 N 4.",
                "Type": {
                    "en": null,
                    "ru": null
                },
                "References": null,
                "OtherCol": "КБП F-345"
            },
            "History": {
                "ReceivedFrom": {
                    "en": "MSU, KBP F-345",
                    "ru": "МГУ, КБП F-345"
                },
                "ReceivedAs": "Penicillium scabrosum",
                "ReceivedDate": "2024-06-13",
                "TypeOfSubstrate": {
                    "en": "insect",
                    "ru": "насекомое"
                },
                "IsolatedFrom": {
                    "en": "ant",
                    "ru": "муравей"
                },
                "AnatomicPart": {
                    "en": null,
                    "ru": null
                },
                "Location": {
                    "en": null,
                    "ru": null
                },
                "Geographics": {
                    "en": "Novgorod Region",
                    "ru": "Новгородская область"
                },
                "Country": {
                    "en": "Russia",
                    "ru": "Россия"
                },
                "IsolationDate": "2023-10-01",
                "IsolateNumber": {
                    "en": null,
                    "ru": null
                }
            },
            "CultivationAndStorage": {
                "IncubationTemp": 25,
                "GrowthMedium": 12,
                "GrowthCondition": {
                    "en": null,
                    "ru": null
                }
            },
            "StrainCharacteristics": {
                "EnzymeProduction": {
                    "en": null,
                    "ru": null
                },
                "MetaboliteProduction": {
                    "en": null,
                    "ru": null
                },
                "Transformation": {
                    "en": null,
                    "ru": null
                },
                "Degradation": {
                    "en": null,
                    "ru": null
                },
                "DNA_Sequence_Accession_Numbers": null
            },
            "GeneralInformation": null
        }
        ```
    - **Ответ (успешный запрос для авторизованного пользователя, HTTP_200_OK):**
      - ```json
        {
            "strain_id": 4,
            "NameAndTaxonomy": {
                "VKM_number": {
                    "CollectionCode": "VKM",
                    "Subcollection": "F",
                    "Strain": 5048
                },
                "Subcollection1": "F",
                "Genus": "Penicillium",
                "Species": "scabrosum",
                "Variant": null,
                "Forma": null,
                "FormaSpecies": null,
                "AuthoritySp": "Frisvad, Samson et Stolk 1990",
                "AuthoritySubSp": null,
                "Family": "Aspergillaceae",
                "Order": "Eurotiales",
                "Class": "Eurotiomycetes",
                "Synonym": null,
                "TaxonomicID": 136735,
                "CurrentName": null,
                "Link_to_TaxonomicID": "https://www.mycobank.org/page/Name%20details%20page/field/Mycobank%20%23/136735#https://www.mycobank.org/page/Name details page/field/Mycobank %23/136735#",
                "Pathogenicgroup": "4",
                "RiskGroup": "no",
                "SanPin": "Данный штамм относится к виду, который включен в 4-ую группу патогенности по СанПиН 3.3686-21, утв. Постановлением Главного государственного санитарного врача РФ от 28.01.2021 N 4.",
                "State": null,
                "Type": {
                    "en": null,
                    "ru": null
                },
                "Qouts": null,
                "OtherName": null,
                "ClassShort": null,
                "References": null,
                "References_nc": null,
                "Race": null,
                "Serovar": null,
                "OtherCol": "КБП F-345"
            },
            "History": {
                "ReceivedFrom": {
                    "en": "MSU, KBP F-345",
                    "ru": "МГУ, КБП F-345"
                },
                "Depositor": {
                    "en": null,
                    "ru": null
                },
                "ReceivedAs": "Penicillium scabrosum",
                "ReceivedDate": "2024-06-13",
                "AccessionDate": null,
                "TypeOfSubstrate": {
                    "en": "insect",
                    "ru": "насекомое"
                },
                "IsolatedFrom": {
                    "en": "ant",
                    "ru": "муравей"
                },
                "AnatomicPart": {
                    "en": null,
                    "ru": null
                },
                "Location": {
                    "en": null,
                    "ru": null
                },
                "Geographics": {
                    "en": "Novgorod Region",
                    "ru": "Новгородская область"
                },
                "Country": {
                    "en": "Russia",
                    "ru": "Россия"
                },
                "USSR": null,
                "CollectedBy": {
                    "en": null,
                    "ru": null
                },
                "CollectedDate": null,
                "IsolationDate": "2023-10-01",
                "IsolatedBy": {
                    "en": "Alexeeva P.A., Bochkov D.A.",
                    "ru": "Алексеева П.А., Бочков Д.А."
                },
                "IsolateNumber": {
                    "en": null,
                    "ru": null
                },
                "IdentificateBy": {
                    "en": "Bochkov D.A.",
                    "ru": "Бочков Д.А."
                },
                "IdentificateDate": null
            },
            "CultivationAndStorage": {
                "IncubationTemp": 25,
                "Tested_temperature_growth_range": null,
                "GrowthMedium": 12,
                "GrowthCondition": {
                    "en": null,
                    "ru": null
                },
                "StorageMethods": null,
                "StorageFreeze": null,
                "StorageOil": null,
                "StorageSilicagel": null,
                "StorageWater": null,
                "StorageNitrogen": null,
                "StorageSubcultivation": null,
                "StorageSoil": null
            },
            "StrainCharacteristics": {
                "EnzymeProduction": {
                    "en": null,
                    "ru": null
                },
                "MetaboliteProduction": {
                    "en": null,
                    "ru": null
                },
                "Transformation": {
                    "en": null,
                    "ru": null
                },
                "Degradation": {
                    "en": null,
                    "ru": null
                },
                "Other": {
                    "en": null,
                    "ru": null
                },
                "MatingType": null,
                "DNA_Sequence_Accession_Numbers": null
            },
            "GeneralInformation": {
                "Latitude": null,
                "Longitude": null,
                "Altitude": null,
                "Curator": "aad",
                "Category": null,
                "Restrictions_on_use": null,
                "Remarks": "cat",
                "EntryDate": "2024-06-14",
                "EditDate": "2024-06-14",
                "Reidentif": {
                    "en": null,
                    "ru": null
                },
                "Confidential_Information": null,
                "Application": {
                    "en": null,
                    "ru": null
                },
                "Form_of_supply": null,
                "Report2020": null,
                "Report2021": null
            }
        }
        ```
    - **Ответ (ошибка, например, штамм не найден или у пользователя нет прав просматривать штамм, HTTP_404_NOT_FOUND):**
        ```json
        {
            "error": {
                "ru": "Штамм не найден",
                "en": "Strain not found"
            }
        }
        ```


- **`[GET] /api/strains/get_strains/`** – *Получение списка всех штаммов.*
    - **Описание:** Этот эндпоинт используется для получения списка всех штаммов. Можно использовать параметры `offset`
      и `limit` для пагинации.
    - **Параметры:**
        - `offset` (по умолчанию 0) – Начальная позиция для выборки.
        - `limit` (по умолчанию 100) – Максимальное количество записей для выборки.
    - **Ответ (успешный запрос для запроса: '/api/strains/get_strains/?limit=5&offset=5', HTTP_200_OK):**
    - ```json 
      {
        "count": 7306,
        "next": "http://localhost:8000/api/strains/get_strains/?limit=5&offset=5",
        "previous": null,
        "results": [
            {
                "strain_id": 1,
                "VKM_number": {
                    "CollectionCode": "VKM",
                    "Subcollection": "F",
                    "Strain": 1566
                },
                "Genus": "Penicillium",
                "Species": "simplicissimum",
                "Variant": null,
                "AuthoritySp": "(Oudemans 1903) Thom 1930",
                "TypeOfSubstrate": {
                    "en": "soil",
                    "ru": "почва"
                },
                "Country": {
                    "en": "Vietnam",
                    "ru": "Вьетнам"
                },
                "IsolationDate": "2023-07-25"
            },
            {
                "strain_id": 2,
                "VKM_number": {
                    "CollectionCode": "VKM",
                    "Subcollection": "F",
                    "Strain": 4926
                },
                "Genus": "Oidiodendron",
                "Species": "tenuissimum",
                "Variant": null,
                "AuthoritySp": "(Peck 1893) S. Hughes 1958",
                "TypeOfSubstrate": {
                    "en": "ground",
                    "ru": "грунт"
                },
                "Country": {
                    "en": "Russia",
                    "ru": "Россия"
                },
                "IsolationDate": "2022-02-22"
            },
            {
                "strain_id": 3,
                "VKM_number": {
                    "CollectionCode": "VKM",
                    "Subcollection": "F",
                    "Strain": 4970
                },
                "Genus": "Penicillium",
                "Species": "verruculosum",
                "Variant": null,
                "AuthoritySp": "Peyronel 1913",
                "TypeOfSubstrate": {
                    "en": "mutant",
                    "ru": "мутант"
                },
                "Country": {
                    "en": "Russia",
                    "ru": "Россия"
                },
                "IsolationDate": null
            },
            {
                "strain_id": 4,
                "VKM_number": {
                    "CollectionCode": "VKM",
                    "Subcollection": "F",
                    "Strain": 5048
                },
                "Genus": "Penicillium",
                "Species": "scabrosum",
                "Variant": null,
                "AuthoritySp": "Frisvad, Samson et Stolk 1990",
                "TypeOfSubstrate": {
                    "en": "insect",
                    "ru": "насекомое"
                },
                "Country": {
                    "en": "Russia",
                    "ru": "Россия"
                },
                "IsolationDate": "2023-10-01"
            },
            {
                "strain_id": 5,
                "VKM_number": {
                    "CollectionCode": "VKM",
                    "Subcollection": "F",
                    "Strain": 4955
                },
                "Genus": "Pragmopora",
                "Species": "sp.",
                "Variant": null,
                "AuthoritySp": null,
                "TypeOfSubstrate": {
                    "en": "lichen",
                    "ru": "лишайник"
                },
                "Country": {
                    "en": "Russia",
                    "ru": "Россия"
                },
                "IsolationDate": null
            }
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
                "VKM_number": {
                    "CollectionCode": "VKM",
                    "Subcollection": "F",
                    "Strain": 1566
                },
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
    - **Ответ (ошибка, недостаточно прав, HTTP_403_FORBIDDEN):**
      ```json
      {
        "detail": "You do not have permission to perform this action."
      }
      ```
      
- **`[GET] /api/strains/get_my_changed_strains/`** – *Получение списка измененных штаммов текущего пользователя.*
    - **Описание:** Этот эндпоинт используется для получения списка измененных штаммов текущего пользователя. Можно
      использовать параметры `offset` и `limit` для пагинации.
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
            "approved": false,
            "message": "string"
          }
          
            // ... другие штаммы
        ]
      }
      ```
    - **Ответ (ошибка, недостаточно прав, HTTP_403_FORBIDDEN):**
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
            "approved": false,
            "message": "string"
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
      
- **`[GET] /api/strains/get_my_new_strains/`** – *Получение списка новых штаммов текущего пользователя.*
    - **Описание:** Этот эндпоинт используется для получения списка новых штаммов текущего пользователя. Можно использовать
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
            "approved": false,
            "message": "string"
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


#### Эндпоинты связанные с изменением и добавлением:
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
    - **Ответ (ошибка, например, недостаточно прав, HTTP_400_BAD_REQUEST):**
        ```json
        {
           "field_name": "field_error",
           "field_name2": "field_error2"
           // и так далее,
        }
        ```
      

- **`[POST] /api/strains/{strain_id_param}/edit/approve`** – *Редактирование информации о штамме.*
    - **Описание:** Этот эндпоинт используется для одобрения редактирования информации о конкретном штамме по его ID.
    - **Параметры:**
        - `strain_id` – ID штамма, информацию о котором нужно редактировать.
    - **Тело запроса(POST):**
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
- **`[POST] /api/strains/{strain_id_param}/edit/reject`** – *Редактирование информации о штамме.*
    - **Описание:** Этот эндпоинт используется для отклонения редактирования информации о конкретном штамме по его ID, а также позволяет дать комментарий.
    - **Параметры:**
        - `strain_id` – ID штамма, информацию о котором нужно редактировать.
    - **Тело запроса(POST):**
        ```json
        {
            "change_request_id": 1,
            "message": "string"
        }
        ```
    - **Ответ (успешный запрос, HTTP_200_OK):**
        ```json
        {
            "message": {
                "ru": "Запрос на изменение отклонен",
                "en": "Change request rejected"
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
    - ```json
        {
            "field_name": "field_error",
            "field_name2": "field_error2"
            // и так далее
        }
        ```

- **`[POST] /api/strains/add/approve`** – *Одобрение на добавление нового штамма*
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

- **`[POST] /api/strains/add/reject`** – *Отклонение на добавление нового штамма*
    - **Описание:** Этот эндпоинт используется для отклонения добавления нового штамма в систему, а также позволяет дать комментарий.
    - **Тело запроса(PUT):**
        ```json
        {
            "new_request_id": 1,
            "message": "string"
        }
        ```
    - **Ответ (успешный запрос, HTTP_200_OK):**
        ```json
        {
            "message": {
                "ru": "Запрос на добавление отклонен",
                "en": "Add request rejected"
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

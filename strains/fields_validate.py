from .models import StrainModel
from datetime import datetime
import re


def parse_date(date_str):
    if date_str is None:
        return None
    try:
        parsed_data = datetime.strptime(date_str.strip(), "%m/%d/%Y").date()
        return parsed_data.strftime("%Y-%m-%d")
    except ValueError:
        return None


# pattern 1 Только английский язык, всегда начинается с заглавной буквы
# pattern 2 Только английский язык, всегда с маленькой буквы
# pattern 3 Только английский язык
# pattern 4 Только английский язык, запрещен символ '&'
# pattern 5 Только числа
# pattern 6 Только английский язык, запрещен символ ';'
# pattern 7 Только числа, запрещен символ ';'
# pattern 8 запрещен знак ','
# pattern 9 Только русский язык, всегда начинается с заглавной буквы
# pattern 10 Дата в формате YYYY-MM-DD
# pattern 11 Только русский, запрещен символ ';'
# pattern 12 Только русский язык, всегда начинается с заглавной буквы, запрещен символ ';'
# pattern 13 Только английский язык, всегда начинается с заглавной буквы, запрещен символ ';'
# pattern 14 только русский

def try_validate_changes(value, errors):
    strain_model_fields = [field.name for field in StrainModel._meta.fields]
    #В се регулярные выражения для паттернов
    patterns = {
        "pattern1": r'^[A-Z][^А-Яа-я]*$',
        "pattern2": r'^[^А-Яа-яA-Z]*$',
        "pattern3": r'^[^А-Яа-я]*$',
        "pattern4": r'^[^А-Яа-я&]*$',
        "pattern5": r"^\d+$",
        "pattern6": r'^[^А-Яа-я;]*$',
        "pattern7": r'^[0-9, ]*$',
        "pattern8": r'^[^,]*$',
        "pattern9": r'^[А-Я][^A-Za-z]*$',
        "pattern10": r'^\d{4}-\d{2}-\d{2}$',
        "pattern11": r'^[^A-Za-z;]*$',
        "pattern12": r"^[^A-Za-z;]*$",
        "pattern13": r"^[^А-Яа-яЁё;]*$",
        "pattern14": r"^[А-ЯЁ][а-яё]*$"
    }

    # Проверяем, что все поля в value существуют в модели StrainModel
    for field, field_value in value.items():
        if field not in strain_model_fields:
            errors[field] = f"Поле '{field}' не существует в модели StrainModel."

    # Проверяем, что все поля в value имеют правильный формат
    sub_collection1 = value.get("Subcollection1", None)
    if sub_collection1 is not None:
        if sub_collection1 not in ["F", "FW"]:
            errors["Subcollection1"] = "Поле 'Subcollection1' должно быть равно 'F' или 'FW'."

    genus = value.get("Genus", None)
    if genus is not None:
        if re.match(patterns["pattern1"], genus) is None:
            errors["Genus"] = "Поле 'Genus' должно начинаться с заглавной буквы и содержать только латинский алфавит."

    species = value.get("Species", None)
    if species is not None:
        if re.match(patterns["pattern2"], species) is None:
            errors["Species"] = ("Поле 'Species' должно начинаться с маленькой буквы и содержать только латинский "
                                 "алфавит.")

    variant = value.get("Variant", None)
    if variant is not None:
        if re.match(patterns["pattern2"], variant) is None:
            errors["Variant"] = ("Поле 'Variant' должно начинаться с маленькой буквы и содержать только латинский "
                                 "алфавит.")

    forma = value.get("Forma", None)
    if forma is not None:
        if re.match(patterns["pattern2"], forma) is None:
            errors["Forma"] = "Поле 'Forma' должно начинаться с маленькой буквы и содержать только латинский алфавит."

    forma_species = value.get("FormaSpecies", None)
    if forma_species is not None:
        if re.match(patterns["pattern3"], forma_species) is None:
            errors["FormaSpecies"] = "Поле 'FormaSpecies' должно содержать только латинский алфавит."

    strain = value.get("Strain", None)
    if strain is not None:
        try:
            strain = int()
        except ValueError:
            errors["Strain"] = f"Поле 'Strain' должно быть целым числом."

    authority_sp = value.get("AuthoritySp", None)
    if authority_sp is not None:
        if re.match(patterns["pattern4"], authority_sp) is None:
            errors["AuthoritySp"] = ("Поле 'AuthoritySp' должно содержать только латинский"
                                     " алфавит и не допустим символ '&'.")

    authority_sub_sp = value.get("AuthoritySubSp", None)
    if authority_sub_sp is not None:
        if re.match(patterns["pattern4"], authority_sub_sp) is None:
            errors["AuthoritySubSp"] = ("Поле 'AuthoritySubSp' должно содержать только латинский"
                                        " алфавит и не допустим символ '&'.")

    family = value.get("Family", None)
    if family is not None:
        if re.match(patterns["pattern1"], family) is None:
            errors["Family"] = "Поле 'Family' должно начинаться с заглавной буквы и содержать только латинский алфавит."

    order = value.get("Order", None)
    if order is not None:
        if re.match(patterns["pattern1"], order) is None:
            errors["Order"] = "Поле 'Order' должно начинаться с заглавной буквы и содержать только латинский алфавит."

    class_is = value.get("Class", None)
    if class_is is not None:
        if re.match(patterns["pattern1"], class_is) is None:
            errors["Class"] = "Поле 'Class' должно начинаться с заглавной буквы и содержать только латинский алфавит."

    synonym = value.get("Synonym", None)
    if synonym is not None:
        if re.match(patterns["pattern3"], synonym) is None:
            errors["Synonym"] = "Поле 'Synonym' должно содержать только латинский алфавит."

    taxonomic_id = value.get("TaxonomicID", None)
    if taxonomic_id is not None:
        try:
            int(taxonomic_id)
        except ValueError:
            errors["TaxonomicID"] = "Поле 'TaxonomicID' должно быть целым числом."

    current_name = value.get("CurrentName", None)
    if current_name is not None:
        if re.match(patterns["pattern1"], current_name) is None:
            errors["CurrentName"] = ("Поле 'CurrentName' должно начинаться с заглавной буквы и "
                                     "содержать только латинский алфавит.")

    if taxonomic_id is not None:
        link = f"https://www.mycobank.org/page/Name%20details%20page/field/Mycobank%20%23/{taxonomic_id}"
        value["Link_to_TaxonomicID"] = link

    pathogenic_group = value.get("PathogenicGroup", None)
    if pathogenic_group is not None:
        allowed_anthologies = ['no', '1', '2', '3', '4']
        if pathogenic_group not in allowed_anthologies:
            errors["PathogenicGroup"] = "Поле 'PathogenicGroup' должно быть равно 'no' или числом от 1 до 4."

    risk_group = value.get("RiskGroup", None)
    if risk_group is not None:
        allowed_anthologies = ['no', 'BSL-1', 'BSL-2', 'BSL-3', 'BSL-4']
        if risk_group not in allowed_anthologies:
            errors["RiskGroup"] = "Поле 'RiskGroup' должно быть равно 'no' или BSL-1, BSL-2, BSL-3, BSL-4."

    type_rus = value.get("TypeRus", None)
    if type_rus is not None:
        allowed_anthologies = ['нет', 'Тип', 'Голотип', 'Лектотип', 'Изотип', 'Синтип', 'Неотип', 'Паратип']
        if type_rus not in allowed_anthologies:
            errors["TypeRus"] = "Поле 'TypeRus' должно быть равно 'нет' или Тип, Голотип, Лектотип, Изотип, Синтип, " \
                                "Неотип, Паратип."

    type_eng = value.get("TypeEng", None)
    if type_eng is not None:
        allowed_anthologies = ['no', 'Type', 'Holotype', 'Lectotype', 'Isotype', 'Syntype', 'Neotype', 'Paratype']
        if type_eng not in allowed_anthologies:
            errors["TypeEng"] = "Поле 'TypeEng' должно быть равно 'no' или Holotype, Isotype, Neotype, Paratype."

    qouts = value.get("Qouts", None)
    if qouts is not None:
        if re.match(patterns["pattern1"], qouts) is None:
            errors["Qouts"] = "Поле 'Qouts' должно начинаться с заглавной буквы и содержать только латинский алфавит."

    other_name = value.get("OtherName", None)
    if other_name is not None:
        if re.match(patterns["pattern6"], other_name) is None:
            errors["OtherName"] = "Поле 'OtherName' должно содержать только латинский алфавит и не допустим символ ';'."

    references = value.get("References", None)
    if references is not None:
        if re.match(patterns["pattern7"], references) is None:
            errors["References"] = "Поле 'References' должно содержать только числа и недопустим символ ';'."

    references_nc = value.get("References_8nc", None)
    if references_nc is not None:
        if re.match(patterns["pattern7"], references_nc) is None:
            errors["References-nc"] = "Поле 'References-nc' должно содержать только числа и недопустим символ ';'."

    other_col = value.get("OtherCol", None)
    if other_col is not None:
        if re.match(patterns["pattern8"], other_col) is None:
            errors["OtherCol"] = "Поле 'OtherCol' недопустим символ ','"

    # received_from_rus = value.get("ReceivedFromRus", None)
    # if received_from_rus is not None:
    #     if re.match(patterns["pattern11"], received_from_rus) is None:
    #         errors["ReceivedFromRus"] = ("Поле 'ReceivedFromRus' должно содержать только русский язык и недопустим "
    #                                      "символ ';'.")

    received_from_eng = value.get("ReceivedFromEng", None)
    if received_from_eng is not None:
        if re.match(patterns["pattern6"], received_from_eng) is None:
            errors["ReceivedFromEng"] = ("Поле 'ReceivedFromEng' должно содержать только латинский алфавит, "
                                         "также запрещен символ ';'.")

    depositor_rus = value.get("DepositorRus", None)
    if depositor_rus is not None:
        if re.match(patterns["pattern9"], depositor_rus) is None:
            errors["DepositorRus"] = ("Поле 'DepositorRus' должно содержать только русский язык и начинаться с "
                                      "заглавной буквы.")

    depositor_eng = value.get("DepositorEng", None)
    if depositor_eng is not None:
        if re.match(patterns["pattern1"], depositor_eng) is None:
            errors["DepositorEng"] = ("Поле 'DepositorEng' должно начинаться с заглавной буквы и содержать только "
                                      "латинский алфавит.")

    received_as = value.get("ReceivedAs", None)
    if received_as is not None:
        if re.match(patterns["pattern1"], received_as) is None:
            errors["ReceivedAs"] = ("Поле 'ReceivedAs' должно начинаться с заглавной буквы и содержать только "
                                    "латинский алфавит.")

    received_date = value.get("ReceivedDate", None)
    if received_date is not None:
        parsed_received_date = parse_date(received_date)
        if re.match(patterns["pattern10"], parsed_received_date) is None:
            errors["ReceivedDate"] = "Поле 'ReceivedDate' должно быть в формате YYYY-MM-DD."

    accession_date = value.get("AccessionDate", None)
    if accession_date is not None:
        parsed_accession_date = parse_date(accession_date)
        if re.match(patterns["pattern10"], parsed_accession_date) is None:
            errors["AccessionDate"] = "Поле 'AccessionDate' должно быть в формате YYYY-MM-DD."

    # isolated_from_rus = value.get("IsolatedFromRus", None)
    # if isolated_from_rus is not None:
    #     if re.match(patterns["pattern11"], isolated_from_rus) is None:
    #         errors["IsolatedFromRus"] = ("Поле 'IsolatedFromRus' должно содержать только русский язык и недопустим "
    #                                      "символ ';'.")

    # isolated_from_eng = value.get("IsolatedFromEng", None)
    # if isolated_from_eng is not None:
    #     if re.match(patterns["pattern6"], isolated_from_eng) is None:
    #         errors["IsolatedFromEng"] = ("Поле 'IsolatedFromEng' должно содержать только латинский алфавит, "
    #                                      "также запрещен символ ';'.")

    anatomic_part_rus = value.get("AnatomicPartRus", None)
    if anatomic_part_rus is not None:
        if re.match(patterns["pattern11"], anatomic_part_rus) is None:
            errors["AnatomicPartRus"] = ("Поле 'AnatomicPartRus' должно содержать только русский язык и недопустим "
                                         "символ ';'.")

    anatomic_part_eng = value.get("AnatomicPartEng", None)
    if anatomic_part_eng is not None:
        if re.match(patterns["pattern6"], anatomic_part_eng) is None:
            errors["AnatomicPartEng"] = ("Поле 'AnatomicPartEng' должно содержать только латинский алфавит, "
                                         "также запрещен символ ';'.")

    # location_rus = value.get("LocationRus", None)
    # if location_rus is not None:
    #     if re.match(patterns["pattern11"], location_rus) is None:
    #         errors["LocationRus"] = ("Поле 'LocationRus' должно содержать только русский язык и недопустим "
    #                                  "символ ';'.")

    location_eng = value.get("LocationEng", None)
    if location_eng is not None:
        if re.match(patterns["pattern6"], location_eng) is None:
            errors["LocationEng"] = ("Поле 'LocationEng' должно содержать только латинский алфавит, "
                                     "также запрещен символ ';'.")

    geographics_rus = value.get("GeographicsRus", None)
    if geographics_rus is not None:
        if re.match(patterns["pattern11"], geographics_rus) is None:
            errors["GeographicsRus"] = ("Поле 'GeographicsRus' должно содержать только русский язык и недопустим "
                                        "символ ';'.")

    geographics_eng = value.get("GeographicsEng", None)
    if geographics_eng is not None:
        if re.match(patterns["pattern6"], geographics_eng) is None:
            errors["GeographicsEng"] = ("Поле 'GeographicsEng' должно содержать только латинский алфавит, "
                                        "также запрещен символ ';'.")

    country_rus = value.get("CountryRus", None)
    if country_rus is not None:
        if re.match(patterns["pattern11"], country_rus) is None:
            errors["CountryRus"] = ("Поле 'CountryRus' должно содержать только русский язык и недопустим "
                                    "символ ';'.")

    country_eng = value.get("CountryEng", None)
    if country_eng is not None:
        if re.match(patterns["pattern6"], country_eng) is None:
            errors["CountryEng"] = ("Поле 'CountryEng' должно содержать только латинский алфавит, "
                                    "также запрещен символ ';'.")

    collected_by_rus = value.get("CollectedByRus", None)
    if collected_by_rus is not None:
        if re.match(patterns["pattern11"], collected_by_rus) is None:
            errors["CollectedByRus"] = ("Поле 'CollectedByRus' должно содержать только русский язык и недопустим "
                                        "символ ';'.")

    collected_by_eng = value.get("CollectedByEng", None)
    if collected_by_eng is not None:
        if re.match(patterns["pattern6"], collected_by_eng) is None:
            errors["CollectedByEng"] = ("Поле 'CollectedByEng' должно содержать только латинский алфавит, "
                                        "также запрещен символ ';'.")

    collected_date = value.get("CollectedDate", None)
    if collected_date is not None:
        parsed_collected_date = parse_date(collected_date)
        if re.match(patterns["pattern10"], parsed_collected_date) is None:
            errors["CollectedDate"] = "Поле 'CollectedDate' должно быть в формате YYYY-MM-DD."

    isolation_date = value.get("IsolationDate", None)
    if isolation_date is not None:
        parsed_isolation_date = parse_date(isolation_date)
        if re.match(patterns["pattern10"], parsed_isolation_date) is None:
            errors["IsolationDate"] = "Поле 'IsolationDate' должно быть в формате YYYY-MM-DD."

    isolated_by_rus = value.get("IsolatedByRus", None)
    if isolated_by_rus is not None:
        if re.match(patterns["pattern11"], isolated_by_rus) is None:
            errors["IsolatedByRus"] = ("Поле 'IsolatedByRus' должно содержать только русский язык и недопустим "
                                       "символ ';'.")

    isolated_by_eng = value.get("IsolatedByEng", None)
    if isolated_by_eng is not None:
        if re.match(patterns["pattern6"], isolated_by_eng) is None:
            errors["IsolatedByEng"] = ("Поле 'IsolatedByEng' должно содержать только латинский алфавит, "
                                       "также запрещен символ ';'.")

    isolate_number_eng = value.get("IsolateNumberEng", None)
    if isolate_number_eng is not None:
        if re.match(patterns["pattern3"], isolate_number_eng) is None:
            errors["IsolateNumberEng"] = "Поле 'IsolateNumberEng' должно содержать только латинский алфавит."

    identificate_by_rus = value.get("IdentificateByRus", None)
    if identificate_by_rus is not None:
        if re.match(patterns["pattern12"], identificate_by_rus) is None:
            errors["IdentificateByRus"] = ("Поле 'IdentificateByRus' должно содержать только русский язык и начинаться "
                                           "с заглавной буквы, также запрещен символ ';'.")

    identificate_by_eng = value.get("IdentificateByEng", None)
    if identificate_by_eng is not None:
        if re.match(patterns["pattern13"], identificate_by_eng) is None:
            errors["IdentificateByEng"] = ("Поле 'IdentificateByEng' должно содержать только латинский алфавит и "
                                           "начинаться с заглавной буквы, также запрещен символ ';'.")

    # identificate_date = value.get("IdentificateDate", None)
    # if identificate_date is not None:
    #     if re.match(patterns["pattern10"], identificate_date) is None:
    #         errors["IdentificateDate"] = "Поле 'IdentificateDate' должно быть в формате YYYY-MM-DD."

    incubation_temp = value.get("IncubationTemp", None)
    if incubation_temp is not None:
        try:
            int(incubation_temp)
        except ValueError:
            errors["IncubationTemp"] = "Поле 'IncubationTemp' должно быть числом."

    growth_medium = value.get("GrowthMedium", None)
    if growth_medium is not None:
        try:
            int(growth_medium)
        except ValueError:
            errors["GrowthMedium"] = "Поле 'GrowthMedium' должно быть числом."

    growth_condition_rus = value.get("GrowthConditionRus", None)
    if growth_condition_rus is not None:
        if re.match(patterns["pattern14"], growth_condition_rus) is None:
            errors["GrowthConditionRus"] = "Поле 'GrowthConditionRus' должно содержать только русский алфавит."

    growth_condition_eng = value.get("GrowthConditionEng", None)
    if growth_condition_eng is not None:
        if re.match(patterns["pattern3"], growth_condition_eng) is None:
            errors["GrowthConditionEng"] = "Поле 'GrowthConditionEng' должно содержать только латинский алфавит."

    storage_methods = value.get("StorageMethods", None)
    if storage_methods is not None:
        if re.match(patterns["pattern6"], storage_methods) is None:
            errors["StorageMethods"] = ("Поле 'StorageMethods' должно содержать только латинский алфавит, "
                                        "также запрещен символ ';'.")

    storage_freeze = value.get("StorageFreeze", None)
    if storage_freeze is not None:
        if re.match(patterns["pattern6"], storage_freeze) is None:
            errors["StorageFreeze"] = ("Поле 'StorageFreeze' должно содержать только латинский алфавит, "
                                       "также запрещен символ ';'.")

    # storage_oil = value.get("StorageOil", None)
    # if storage_oil is not None:
    #     if re.match(patterns["pattern6"], storage_oil) is None:
    #         errors["StorageOil"] = ("Поле 'StorageOil' должно содержать только латинский алфавит, "
    #                                 "также запрещен символ ';'.")

    storage_silicagel = value.get("StorageSilicagel", None)
    if storage_silicagel is not None:
        if re.match(patterns["pattern6"], storage_silicagel) is None:
            errors["StorageSilicagel"] = ("Поле 'StorageSilicagel' должно содержать только латинский алфавит, "
                                          "также запрещен символ ';'.")

    storage_water = value.get("StorageWater", None)
    if storage_water is not None:
        if re.match(patterns["pattern6"], storage_water) is None:
            errors["StorageWater"] = ("Поле 'StorageWater' должно содержать только латинский алфавит, "
                                      "также запрещен символ ';'.")

    # storage_nitrogen = value.get("StorageNitrogen", None)
    # if storage_nitrogen is not None:
    #     if re.match(patterns["pattern6"], storage_nitrogen) is None:
    #         errors["StorageNitrogen"] = ("Поле 'StorageNitrogen' должно содержать только латинский алфавит, "
    #                                      "также запрещен символ ';'.")

    storage_subcultivation = value.get("StorageSubcultivation", None)
    if storage_subcultivation is not None:
        if re.match(patterns["pattern6"], storage_subcultivation) is None:
            errors["StorageSubcultivation"] = (
                "Поле 'StorageSubcultivation' должно содержать только латинский алфавит, "
                "также запрещен символ ';'.")

    storage_soil = value.get("StorageSoil", None)
    if storage_soil is not None:
        if re.match(patterns["pattern6"], storage_soil) is None:
            errors["StorageSoil"] = ("Поле 'StorageSoil' должно содержать только латинский алфавит, "
                                     "также запрещен символ ';'.")

    enzyme_production_eng = value.get("EnzymeProductionEng", None)
    if enzyme_production_eng is not None:
        if re.match(patterns["pattern6"], enzyme_production_eng) is None:
            errors["EnzymeProductionEng"] = ("Поле 'EnzymeProductionEng' должно содержать только латинский алфавит, "
                                             "также запрещен символ ';'.")

    metabolite_production_eng = value.get("MetaboliteProductionEng", None)
    if metabolite_production_eng is not None:
        if re.match(patterns["pattern6"], metabolite_production_eng) is None:
            errors["MetaboliteProductionEng"] = ("Поле 'MetaboliteProductionEng' должно содержать только латинский "
                                                 "алфавит, также запрещен символ ';'.")

    transformation_eng = value.get("TransformationEng", None)
    if transformation_eng is not None:
        if re.match(patterns["pattern6"], transformation_eng) is None:
            errors["TransformationEng"] = ("Поле 'TransformationEng' должно содержать только латинский алфавит, "
                                           "также запрещен символ ';'.")

    degradation_eng = value.get("DegradationEng", None)
    if degradation_eng is not None:
        if re.match(patterns["pattern6"], degradation_eng) is None:
            errors["DegradationEng"] = ("Поле 'DegradationEng' должно содержать только латинский алфавит, "
                                        "также запрещен символ ';'.")

    # other_rus = value.get("OtherRus", None)
    # if other_rus is not None:
    #     if re.match(patterns["pattern14"], other_rus) is None:
    #         errors["OtherRus"] = "Поле 'OtherRus' должно содержать только русский алфавит."

    other_eng = value.get("OtherEng", None)
    if other_eng is not None:
        if re.match(patterns["pattern3"], other_eng) is None:
            errors["OtherEng"] = "Поле 'OtherEng' должно содержать только латинский алфавит."

    dna_sequence_accession_numbers = value.get("DNA_Sequence_Accession_Numbers", None)
    if dna_sequence_accession_numbers is not None:
        if re.match(patterns["pattern6"], dna_sequence_accession_numbers) is None:
            errors["DNA_Sequence_Accession_Numbers"] = ("Поле 'DNA_Sequence_Accession_Numbers' должно содержать "
                                                        "только латинский алфавит, также запрещен символ ';'.")

    entry_date = value.get("EntryDate", None)
    if entry_date is not None:
        parsed_entry_date = parse_date(entry_date)
        if re.match(patterns["pattern10"], parsed_entry_date) is None:
            errors["EntryDate"] = "Поле 'EntryDate' должно быть в формате YYYY-MM-DD."

    edit_date = value.get("EditDate", None)
    if edit_date is not None:
        parsed_edit_date = parse_date(edit_date)
        if re.match(patterns["pattern10"], parsed_edit_date) is None:
            errors["EditDate"] = "Поле 'EditDate' должно быть в формате YYYY-MM-DD."

    reidentif_rus = value.get("ReidentifRus", None)
    if reidentif_rus is not None:
        if re.match(patterns["pattern12"], reidentif_rus) is None:
            errors["ReidentifRus"] = ("Поле 'ReidentifRus' должно содержать только русский язык и начинаться "
                                      "с заглавной буквы, также запрещен символ ';'.")

    reidentif_eng = value.get("ReidentifEng", None)
    if reidentif_eng is not None:
        if re.match(patterns["pattern13"], reidentif_eng) is None:
            errors["ReidentifEng"] = ("Поле 'ReidentifEng' должно содержать только латинский алфавит и начинаться "
                                      "с заглавной буквы, также запрещен символ ';'.")

    enzyme_production_rus = value.get("EnzymeProductionRus", None)
    if enzyme_production_rus is not None:
        if re.match(patterns["pattern11"], enzyme_production_rus) is None:
            errors["EnzymeProductionRus"] = ("Поле 'EnzymeProductionRus' должно содержать только русский язык и "
                                             "недопустим символ ';'.")

    # metabolite_production_rus = value.get("MetaboliteProductionRus", None)
    # if metabolite_production_rus is not None:
    #     if re.match(patterns["pattern11"], metabolite_production_rus) is None:
    #         errors["MetaboliteProductionRus"] = ("Поле 'MetaboliteProductionRus' должно содержать только русский "
    #                                              "язык и недопустим символ ';'.")

    transformation_rus = value.get("TransformationRus", None)
    if transformation_rus is not None:
        if re.match(patterns["pattern11"], transformation_rus) is None:
            errors["TransformationRus"] = ("Поле 'TransformationRus' должно содержать только русский язык и "
                                           "недопустим символ ';'.")

    degradation_rus = value.get("DegradationRus", None)
    if degradation_rus is not None:
        if re.match(patterns["pattern11"], degradation_rus) is None:
            errors["DegradationRus"] = ("Поле 'DegradationRus' должно содержать только русский язык и "
                                        "недопустим символ ';'.")

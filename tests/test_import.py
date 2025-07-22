import os
import pytest
from utils.db_connect import execute_query_db
from pages_tests.base_test import test_case_parameters
from pages_tests.data_api_import import get_person_id


def test_happy_path(info_api, db_connec):
    person_id = get_person_id()
    
    response = info_api.affter_import(person_id)
    
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

    sql_template_path = os.path.join("utils", "sql_information", "personId_data.sql")
    result = execute_query_db(db_connec, sql_template_path, (person_id,))
    
    assert len(result) > 0, f"El personId {person_id} no esta cargado en la base de datos"
    assert result[0]['personId'] == person_id, f"El personId encontrado no arroja algun resultado correcto"

    print("test_happy_path Passed")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.json()}")
    print(f"Base de datos: {result}")


@pytest.mark.parametrize("person_id, expected_status", test_case_parameters("case_border.json", arg="argumento"))
def test_negative(info_api, person_id, expected_status):
    response = info_api.affter_import(person_id)

    print(f"Caso de prueba negativo ={person_id}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    
    assert response.status_code == expected_status, \
        f"Expected status {expected_status}, got {response.status_code}"
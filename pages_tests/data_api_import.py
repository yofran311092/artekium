import random
import requests
import json
import os
from config_tests.enviroment_data import enviroment_setup


def generate_person_id():
    # Genera un person_Id aleatorio entre 100 y 999, para cambiar la cantidad de caracteres...
    # agregar solo otro numero, ejemplo 1000, 1999
    return random.randint(100, 999)


def get_person_id():
    """
    Pregunta al usuario si desea ingresar el personId manualmente o generar uno dinámicamente
    """
    user_input = input("¿Deseas ingresar el personId manualmente? (si/no): ").strip().lower()

    if user_input == 'si':
        # Si el usuario quiere ingresarlo manualmente, pedimos el personId
        person_id = input("Ingresa el personId manualmente: ").strip()
        while not person_id.isdigit():
            print("El personId debe ser un número.")
            person_id = input("Ingresa el personId manualmente: ").strip()
        person_id = int(person_id)
    else:
        # Si no, usamos el método para generar un personId aleatorio
        person_id = generate_person_id()

    return person_id


class SendApi:

    def __init__(self, env):
        config = enviroment_setup(env)
        self.base_url = config["qa_base_url"]
        self.auth_url = config["qa_auth_url"]
        self.token = self.invoke_token_api()

    def invoke_token_api(self):
        username_data = os.getenv('USER_AUTH')
        password_data = os.getenv('PASS_AUTH')
        with open("pages_tests/authorization_file.json", "r") as f:
            formato = f.read()
        body = formato.replace("{usuario}", username_data).replace("{clave}", password_data)
        data = json.loads(body)
        try:
            response = requests.post(self.auth_url, json=data)
            response.raise_for_status()
            token = response.json().get("access_token")
            return token
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def affter_import(self, person_id):
        token = self.invoke_token_api()
        body = [{"personId": person_id}]
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        try:
            import_url = f"{self.base_url}/import"
            response = requests.post(import_url, json=body, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

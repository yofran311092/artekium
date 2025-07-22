def enviroment_setup(enviroment):
    enviroment_params = {
        "test": {
            "qa_base_url": "https://api.test.worldsys.ar",
            "qa_auth_url": "https://api.auth.test.ar"
        },
        "dev": {
            "dev_base_url": "https://api.dev.worldsys.ar",
            "dev_auth_url": "https://api.auth.dev.ar"
        }
    }
    if enviroment not in enviroment_params:
        raise ValueError(f"El ambiente que has seleccionado es incorrecto: {enviroment}")
    return enviroment_params[enviroment]

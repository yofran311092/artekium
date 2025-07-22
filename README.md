# 🚀 Proyecto de Automatización para ARTEKIUM

## 🚀 Instalación y Configuración

### 1. **Requisitos Previos**

- **Python 3.8+**
- **MySQL Server**
- **Pycharm o cualquier IDE**

### 2. **Instalación**

```bash
# Clonar el proyecto
git clone https://github.com/yofran311092/artekium
```
### 3. **Configuración de Variables de Entorno**

Crear archivo `.env` en la raíz del proyecto:

```env
# Configuración de credenciales para conectarse con SQL
DB_HOST=127.0.0.1:5432
DB_USER=test_user
DB_PASSWORD=TestP@ssw0rd!
DB_NAME=test_database

USER_AUTH=yofran_user
PASS_AUTH=YofranPass123
```

**⚠️ Importante:** Antes de ejecutar los test deberas colocar tus credenciales

## 🧪4. **Ejecucion de Tests**

### **Comando de Ejecución**
```bash
# Ejecutar los test con pytest
pytest test_import.py
```

## 🛠️ **Dependencias**

```txt
Ejecutar esta linea de comando para poder instalar todas las dependencias
        pip install -r requirements.txt  
        
Se pueden agregar a medida que se van utilizando otras librerias en el codigo

```




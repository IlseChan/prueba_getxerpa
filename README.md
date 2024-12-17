API de Enriquecimiento de Transacciones Bancarias 🚀

Este proyecto implementa una API REST desarrollada en Django que permite enriquecer transacciones bancarias con información adicional como categorías y comercios, utilizando keywords para asociar descripciones a datos enriquecidos.

Características Principales 🌟

Enriquecimiento de Transacciones:
Procesa un conjunto de transacciones y agrega automáticamente información de categorías y comercios.

CRUD Completo:

Categorías: Crear, listar, actualizar y eliminar.

Comercios: Crear y asociar a categorías.

Keywords: Crear y asociar a comercios.

Métricas Detalladas 📊:

Al enriquecer transacciones, la API devuelve métricas:

Total de transacciones.

Tasa de categorización.

Tasa de identificación de comercio.

Validación de Datos:

La API valida entradas incorrectas y maneja errores de forma eficiente.


Pruebas de Desempeño:

Capaz de procesar 1,000 transacciones en menos de 8 segundos.


Requisitos Previos ⚙️

Python 3.12+

Django 5.x

SQLite3 (Base de datos por defecto)

Instalación y Configuración 📦

Clonar el repositorio:


git clone [https://github.com/tuusuario/nombre-del-repositorio.git]

cd nombre-del-repositorio


Crear un entorno virtual e instalar dependencias:

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


Realizar migraciones y cargar datos iniciales:

python3 manage.py makemigrations

python3 manage.py migrate

Ejecutar el servidor local:

python3 manage.py runserver


Endpoints Disponibles 🔗

Enriquecimiento de Transacciones

POST /api/enrich/

Request Body:

json



{

  "transactions": [
  
    {
      "id": "1",
      "description": "PYU *UberEats",
      "amount": -300.00,
      "date": "2023-12-01"
    }
  ]
}

Respuesta:

json


{
  "enriched_transactions": [
  
    {
      "id": "1",
      "description": "PYU *UberEats",
      "amount": -300.00,
      "date": "2023-12-01",
      "merchant": "Uber Eats",
      "category": "Restaurantes"
    }
  ],
  "metrics": {
    "total_transactions": 1,
    "categorized_rate": 1.0,
    "merchant_identified_rate": 1.0
  }
}


CRUD Categorías

GET /api/categories/

POST /api/categories/

PUT /api/categories/{id}/

DELETE /api/categories/{id}/

CRUD Comercios

POST /api/merchants/

CRUD Keywords

POST /api/keywords/

GET /api/keywords/

Listar Transacciones

GET /api/transactions/

Pruebas Unitarias 🧪

Ejecuta las pruebas con el siguiente comando:

python3 manage.py test

Autor ✍️
Ilse Karina Chan Alejandre
(https://www.linkedin.com/in/ilse-chan-1328a6233/)
[ilsechan.alejandre@gmail.com]

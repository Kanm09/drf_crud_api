# DRF CRUD API

API REST para gestión de tareas desarrollada con Django REST Framework.

## Características
- CRUD completo para tareas
- Interfaz web con templates
- API REST endpoints

## Tecnologías
- Python 3.x
- Django
- Django REST Framework
- SQLite

## Instalación
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Endpoints
- GET /api/tasks/ - Listar tareas
- POST /api/tasks/ - Crear tarea
- PUT /api/tasks/{id}/ - Actualizar tarea
- DELETE /api/tasks/{id}/ - Eliminar tarea

## Estructura del Proyecto
```
drf_crud_api/
├── manage.py
├── db.sqlite3
├── drfsimplecrud/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── urls.py
    └── templates/
```

## Autor
Desarrollado como parte del plan de estudio Pre-Junior → Junior Backend

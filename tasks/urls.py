from rest_framework import routers
from .api import TasksViewSet
from django.urls import path, include
from .views import list_task, guardar_tarea, eliminar_tarea, editar_tarea, actualizar_tarea

router = routers.DefaultRouter()
router.register('tasks', TasksViewSet, 'task')

urlpatterns = [
    path("", list_task, name="home"),
    path("api/", include(router.urls)),
    path("guardar_tarea/", guardar_tarea, name="Guardar_tarea"),
    path("eliminar_tarea/<int:tarea_id>", eliminar_tarea, name="eliminar_tarea"),
    path("editar_tarea/<int:tarea_id>", editar_tarea, name="editar_tarea"),
    path("actualizar_tarea/<int:tarea_id>", actualizar_tarea, name="actualizar_tarea"),
]
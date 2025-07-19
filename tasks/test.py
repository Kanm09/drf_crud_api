from django.test import TestCase
from .models import Tasks
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TasksTestCase(TestCase):
    def test_guardar_tarea(self):
        titulo = "titulo test"
        descripcion = "descripcion test"
        technology = "python test"

        tarea = Tasks.objects.create(
            titulo = titulo,
            descripcion = descripcion,
            technology = technology
        )
        self.assertEqual(tarea.titulo, titulo)
        self.assertEqual(tarea.descripcion, descripcion)
        self.assertEqual(tarea.technology, technology)

class TasksAPITestCase(APITestCase):
    def setUp(self):
        """ Metodo que se ejecuta antes de cada test """
        # Crear una tarea de prueba para usar en los test
        self.tarea_test = Tasks.objects.create(
            titulo = "titulo api test",
            descripcion = "descripcion api test",
            technology= "tecnologia api test"
        )
    
    def test_get_list_task(self):
        """ Test para obtener lista de tareas via API """
        url = '/api/task/'

        # Act
        response = self.client.get(url)

        # Assert

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Debe haber 1 tarea (la del setUp)

    def test_create_task(self):
        """ Test para crear una nueva tarea con metodo POST """
        url = '/api/tasks/'

        data = {
            'titulo': "Titulo Probando POST",
            'descripcion': "Descripcion probando POST",
            'technology': "python - django"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tasks.objects.count(), 2)

        latest_task = Tasks.objects.latest("id")

        self.assertEqual(latest_task.titulo, data["titulo"])
        self.assertEqual(latest_task.descripcion, data["descripcion"])
        self.assertEqual(latest_task.technology, data["technology"])

    def test_update_task(self):
        """ Test corroborar que se pueda actualizar una tarea """
        url = f"/api/tasks/{self.tarea_test.id}/"

        data = {
            "titulo": "Titulo Probando actualizacion",
            "descripcion": "Descripcion Actualizada",
            "technology": "python - django A",
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.tarea_test.refresh_from_db()

        self.assertEqual(self.tarea_test.titulo, data["titulo"])
        self.assertEqual(self.tarea_test.descripcion, data["descripcion"])
        self.assertEqual(self.tarea_test.technology, data["technology"])

    def test_delete_task(self):
        """ Test para eliminar una tarea """

        url = f'/api/tasks/{self.tarea_test.id}/'

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Tasks.objects.count(), 0)
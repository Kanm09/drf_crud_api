# 🚀 PLAN DE ESTUDIO: Pre-Junior → Junior Backend (8 SEMANAS INTENSIVAS)

**Modalidad:** 4 horas/día × 7 días × 8 semanas = 224 horas totales
**Objetivo:** Nivel Junior Backend Python Django
**Fecha inicio:** 16 de julio 2025

---

## 📊 DIAGNÓSTICO INICIAL (15 julio 2025)
**Score evaluación:** 7/21 puntos (33%)
**Nivel actual:** Pre-Junior
**Nivel objetivo:** Junior (67-80%)

### ✅ FORTALEZAS DETECTADAS:
- Python básico (list comprehensions, diccionarios)
- Django Models (estructura básica, migraciones)
- DRF Serializers (propósito y configuración básica)
- HTTP Methods (GET, POST, PUT, DELETE)
- ORM básico (CRUD simple con Django)

### ❌ GAPS CRÍTICOS A CUBRIR:
- **Git** - Nunca usado (CRÍTICO para trabajo)
- **Testing** - Cero experiencia
- **Deploy** - No ha desplegado aplicaciones
- **DRF avanzado** - ViewSets, validaciones
- **SQL** - No sabe consultas directas

---

## 📅 SEMANA 1: GIT + TESTING FOUNDATIONS

### 🎯 OBJETIVOS:
- Git profesional funcionando
- Tests básicos escritos y pasando
- Primer deploy en producción

### LUNES (4 horas) - Git Setup:
```
09:00-10:00 | Instalar Git + configuración inicial
              git config --global user.name "Tu Nombre"
              git config --global user.email "tu@email.com"

10:00-11:30 | Crear GitHub + subir proyecto actual
              - Crear cuenta GitHub
              - git init en proyecto CRUD
              - git add .
              - git commit -m "Initial commit"
              - git remote add origin [URL]
              - git push -u origin main

11:30-12:30 | .gitignore para Django + primer README
              - Crear .gitignore completo
              - README.md profesional
              - git add, commit, push

12:30-13:00 | Git workflow básico
              - Hacer cambio pequeño
              - git status, add, commit, push
```

### MARTES (4 horas) - Git Profundo:
```
09:00-10:30 | Branches básicos + git merge
              git checkout -b feature/nueva-funcionalidad
              git merge, git branch -d

10:30-12:00 | Historial de commits profesionales
              - Mensajes descriptivos
              - git log --oneline
              - git show [commit]

12:00-13:00 | GitHub Issues + Projects básico
              - Crear issues
              - Labels y milestones
```

### MIÉRCOLES (4 horas) - Testing Introducción:
```
09:00-10:30 | ¿Por qué testing? Conceptos básicos
              - Unit vs Integration vs E2E
              - Django TestCase

10:30-12:30 | Primeros tests de modelos Django
              class ProjectTestCase(TestCase):
                  def test_crear_proyecto(self):
                      proyecto = Project.objects.create(
                          titulo="Test",
                          descripcion="Desc test"
                      )
                      self.assertEqual(proyecto.titulo, "Test")

12:30-13:00 | Ejecutar tests + interpretar resultados
              python manage.py test
```

### JUEVES (4 horas) - API Testing:
```
09:00-11:00 | Tests para endpoints DRF
              from rest_framework.test import APITestCase
              
              class ProjectAPITestCase(APITestCase):
                  def test_get_projects(self):
                      response = self.client.get('/api/tasks/')
                      self.assertEqual(response.status_code, 200)

11:00-12:30 | TestCase avanzado + setUp/tearDown
              def setUp(self):
                  self.project = Project.objects.create(...)

12:30-13:00 | Coverage report básico
              pip install coverage
              coverage run --source='.' manage.py test
              coverage report
```

### VIERNES (4 horas) - Deploy Prep:
```
09:00-10:30 | Variables de entorno + settings.py
              pip install python-decouple
              from decouple import config
              DEBUG = config('DEBUG', default=False, cast=bool)

10:30-12:00 | requirements.txt + configuración producción
              pip freeze > requirements.txt
              ALLOWED_HOSTS, DATABASES config

12:00-13:00 | Base de datos para producción
              PostgreSQL setup
```

### SÁBADO (4 horas) - Primer Deploy:
```
09:00-12:00 | Deploy en Railway/Heroku paso a paso
              - Crear cuenta Railway
              - Conectar GitHub repo
              - Variables de entorno
              - Deploy automático

12:00-13:00 | Testing en producción + troubleshooting
              - Verificar API endpoints
              - Debug logs
```

### DOMINGO (4 horas) - Consolidación:
```
09:00-11:00 | Refactor código con tests
              - Mejorar coverage
              - Refactoring seguro

11:00-12:30 | Documentación + README profesional
              - API documentation
              - Setup instructions

12:30-13:00 | Planning semana siguiente
              - Review objetivos cumplidos
              - Preparar Semana 2
```

### ✅ CHECKPOINT SEMANA 1:
- [ ] Proyecto en GitHub con historial de commits
- [ ] Tests básicos pasando (coverage > 50%)
- [ ] Aplicación desplegada y accesible por URL
- [ ] README profesional
- [ ] Workflow Git dominado

---

## 📅 SEMANA 2: DRF INTERMEDIO + ORM

### 🎯 OBJETIVOS:
- API profesional con validaciones y permisos
- Consultas de base de datos optimizadas
- SQL básico dominado

### LUNES (4 horas) - ViewSets Profundo:
```
09:00-10:30 | ModelViewSet vs APIView diferencias
              - Cuándo usar cada uno
              - Ventajas y desventajas

10:30-12:30 | Custom actions en ViewSets
              @action(detail=True, methods=['post'])
              def completar(self, request, pk=None):
                  tarea = self.get_object()
                  tarea.completada = True
                  tarea.save()
                  return Response({'status': 'completada'})

12:30-13:00 | Routing avanzado con DRF
              - Custom URLs para actions
              - Router configuration
```

### MARTES (4 horas) - Validaciones:
```
09:00-11:00 | Validaciones personalizadas en Serializers
              def validate_titulo(self, value):
                  if len(value) < 3:
                      raise serializers.ValidationError("Muy corto")
                  return value

11:00-12:30 | Field-level vs object-level validation
              def validate(self, data):
                  if data['fecha_inicio'] > data['fecha_fin']:
                      raise serializers.ValidationError("Fechas inválidas")
                  return data

12:30-13:00 | Error handling profesional
              - Custom exception handlers
              - User-friendly error messages
```

### MIÉRCOLES (4 horas) - Permisos:
```
09:00-10:30 | IsAuthenticated, AllowAny, IsOwner
              permission_classes = [IsAuthenticated]

10:30-12:00 | Custom permissions
              class IsOwnerOrReadOnly(BasePermission):
                  def has_object_permission(self, request, view, obj):
                      return obj.owner == request.user

12:00-13:00 | Testing permissions
              - Tests con usuarios autenticados
              - Tests de authorization
```

### JUEVES (4 horas) - ORM Django:
```
09:00-11:00 | .filter(), .exclude(), Q objects
              Project.objects.filter(titulo__icontains='django')
              from django.db.models import Q
              Project.objects.filter(Q(titulo='test') | Q(descripcion='test'))

11:00-12:30 | ForeignKey real + related_name
              class Tarea(models.Model):
                  usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas')

12:30-13:00 | .select_related() vs .prefetch_related()
              - N+1 queries problem
              - Optimización de consultas
```

### VIERNES (4 horas) - Consultas Avanzadas:
```
09:00-11:00 | .annotate() y .aggregate()
              from django.db.models import Count
              User.objects.annotate(num_tareas=Count('tareas'))

11:00-12:30 | Subqueries básicas
              from django.db.models import Subquery, OuterRef

12:30-13:00 | Django Debug Toolbar
              - Instalación y configuración
              - Análisis de queries
```

### SÁBADO (4 horas) - SQL Foundations:
```
09:00-11:00 | SQL básico (SELECT, WHERE, ORDER BY)
              SELECT * FROM tasks_project WHERE titulo LIKE '%django%';
              SELECT titulo, descripcion FROM tasks_project ORDER BY created_at DESC;

11:00-12:30 | JOINS (INNER, LEFT)
              SELECT u.username, t.titulo 
              FROM auth_user u 
              INNER JOIN tasks_project t ON u.id = t.usuario_id;

12:30-13:00 | Traducir ORM a SQL
              - Usar .query para ver SQL generado
              - Comparar ORM vs SQL directo
```

### DOMINGO (4 horas) - Optimización:
```
09:00-11:00 | N+1 queries problem
              - Identificar el problema
              - Soluciones con select_related/prefetch_related

11:00-12:30 | Database indexes básicos
              class Meta:
                  indexes = [
                      models.Index(fields=['titulo']),
                  ]

12:30-13:00 | Refactor proyecto con optimizaciones
              - Aplicar optimizaciones aprendidas
              - Medir mejoras de performance
```

### ✅ CHECKPOINT SEMANA 2:
- [ ] API con validaciones personalizadas funcionando
- [ ] Permisos implementados y testeados
- [ ] Consultas optimizadas (sin N+1 queries)
- [ ] Tests con coverage > 70%
- [ ] SQL básico dominado

---

## 📅 SEMANA 3: JAVASCRIPT + AJAX MASTERY

### 🎯 OBJETIVOS:
- Frontend dinámico sin reloads
- Consumir API desde JavaScript
- UX profesional

### LUNES (4 horas) - JS Moderno:
```
09:00-10:30 | let, const, arrow functions
              const saludar = (nombre) => `Hola ${nombre}`;
              let usuarios = [];
              const API_URL = 'http://localhost:8000/api/';

10:30-12:00 | Promesas y async/await
              const promesa = new Promise((resolve, reject) => {
                  setTimeout(() => resolve("Datos"), 1000);
              });
              
              async function obtenerDatos() {
                  try {
                      const resultado = await promesa;
                      console.log(resultado);
                  } catch (error) {
                      console.error(error);
                  }
              }

12:00-13:00 | DOM manipulation
              document.getElementById('btn').addEventListener('click', () => {
                  document.querySelector('.mensaje').textContent = 'Clicked!';
              });
```

### MARTES (4 horas) - Fetch API:
```
09:00-11:00 | Fetch básico + handling responses
              async function obtenerTareas() {
                  const response = await fetch('/api/tasks/');
                  if (!response.ok) {
                      throw new Error('Error en la respuesta');
                  }
                  const tareas = await response.json();
                  return tareas;
              }

11:00-12:30 | POST, PUT, DELETE con fetch
              async function crearTarea(datos) {
                  const response = await fetch('/api/tasks/', {
                      method: 'POST',
                      headers: {
                          'Content-Type': 'application/json',
                          'X-CSRFToken': getCookie('csrftoken')
                      },
                      body: JSON.stringify(datos)
                  });
                  return response.json();
              }

12:30-13:00 | Error handling en AJAX
              - Try/catch blocks
              - User-friendly error messages
```

### MIÉRCOLES (4 horas) - AJAX CRUD:
```
09:00-11:00 | Crear tareas sin reload
              document.getElementById('form-tarea').addEventListener('submit', async (e) => {
                  e.preventDefault();
                  const formData = new FormData(e.target);
                  const datos = {
                      titulo: formData.get('titulo'),
                      descripcion: formData.get('descripcion')
                  };
                  await crearTarea(datos);
                  await cargarTareas(); // Actualizar lista
              });

11:00-12:30 | Actualizar en tiempo real
              - Editar inline
              - Updates parciales con PATCH

12:30-13:00 | Eliminar con confirmación
              - Confirmación modal
              - Soft deletes
```

### JUEVES (4 horas) - UX Avanzado:
```
09:00-10:30 | Loading states
              function mostrarLoading() {
                  document.getElementById('spinner').classList.remove('d-none');
              }
              
              function ocultarLoading() {
                  document.getElementById('spinner').classList.add('d-none');
              }

10:30-12:00 | Form validation frontend
              - Validación en tiempo real
              - Feedback visual

12:00-13:00 | Error messages user-friendly
              - Toast notifications
              - Inline errors
```

### VIERNES (4 horas) - Integración Completa:
```
09:00-11:00 | CSRF tokens en AJAX
              function getCookie(name) {
                  let cookieValue = null;
                  if (document.cookie && document.cookie !== '') {
                      const cookies = document.cookie.split(';');
                      for (let i = 0; i < cookies.length; i++) {
                          const cookie = cookies[i].trim();
                          if (cookie.substring(0, name.length + 1) === (name + '=')) {
                              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                              break;
                          }
                      }
                  }
                  return cookieValue;
              }

11:00-12:30 | Authentication en frontend
              - Login/logout con AJAX
              - Token storage
              - Authenticated requests

12:30-13:00 | CORS configuration
              - Django CORS headers
              - Preflight requests
```

### SÁBADO (4 horas) - Polish Frontend:
```
09:00-11:00 | Bootstrap components avanzados
              - Modals
              - Tooltips
              - Alerts

11:00-12:30 | Responsive design
              - Mobile-first approach
              - Breakpoints optimization

12:30-13:00 | Accessibility básico
              - ARIA labels
              - Keyboard navigation
```

### DOMINGO (4 horas) - Testing Frontend:
```
09:00-11:00 | Selenium básico
              from selenium import webdriver
              from selenium.webdriver.common.by import By
              
              class FrontendTestCase(StaticLiveServerTestCase):
                  def setUp(self):
                      self.browser = webdriver.Chrome()

11:00-12:30 | E2E tests simples
              - User workflows completos
              - Form submissions

12:30-13:00 | Integration tests completos
              - Frontend + Backend integration
```

### ✅ CHECKPOINT SEMANA 3:
- [ ] CRUD completo sin reloads
- [ ] JavaScript moderno funcionando
- [ ] UX profesional implementada
- [ ] E2E tests básicos
- [ ] Responsive design

---

## 📅 SEMANA 4: PROYECTO COMPLETO + PORTFOLIO

### 🎯 OBJETIVOS:
- Aplicación production-ready completa
- Portfolio GitHub profesional
- Preparación para entrevistas

### LUNES-MIÉRCOLES (12 horas total) - Proyecto Final:
```
PROYECTO: CRUD COMPLETO CON:

Backend:
- API REST con todas las validaciones
- Permisos y authentication
- Tests con coverage > 90%
- Consultas optimizadas
- Deploy automático funcionando

Frontend:
- Interfaz completamente dinámica
- AJAX para todas las operaciones
- UX profesional
- Responsive design
- Error handling completo

DevOps:
- Deploy automático desde Git
- Variables de entorno configuradas
- Monitoring básico
- Logs estructurados

Documentación:
- README completo con screenshots
- API documentation
- Setup instructions
- Architecture overview
```

### JUEVES-VIERNES (8 horas total) - Portfolio GitHub:
```
OBJETIVOS:

3 repositorios principales:
1. CRUD Project (principal)
2. Mini proyecto API-only
3. Mini proyecto Frontend-only

Cada repo debe tener:
- README profesional con:
  * Screenshots/GIFs
  * Tech stack usado
  * Setup instructions
  * Live demo link
  * Architecture explanation
- Commits consistentes
- Issues y milestones
- Releases tagged

Perfil GitHub:
- Bio profesional
- Contribuciones consistentes (green squares)
- Pinned repositories
- Contact information
```

### SÁBADO-DOMINGO (8 horas total) - Preparación Entrevistas:
```
PREPARACIÓN TÉCNICA:

Preguntas comunes Junior Backend:
- Explica el patrón MVC
- ¿Qué es una API REST?
- Diferencia entre GET y POST
- ¿Qué son las migraciones?
- ¿Cómo optimizarías una consulta lenta?
- ¿Qué es Git y por qué es importante?
- Explica tu proyecto más complejo

Live Coding Practice:
- Crear modelo Django básico
- Escribir test simple
- API endpoint básico
- Consulta ORM
- Fix a bug in live code

Proyectos adicionales rápidos:
- API de clima con external API
- Todo list con localStorage
- Calculator con JS
- Simple blog with Django
```

### ✅ CHECKPOINT SEMANA 4:
- [ ] Aplicación completa deployada y funcionando
- [ ] Portfolio GitHub profesional
- [ ] 3+ proyectos documentados
- [ ] Preparación entrevistas completada
- [ ] **LISTO PARA APLICAR A JUNIOR**

---

## 🎯 RESULTADO FINAL (después de 8 semanas):

### TENDRÁS:
✅ Portfolio GitHub con 3+ proyectos profesionales
✅ Aplicación full-stack en producción funcionando
✅ Tests automatizados y CI/CD básico
✅ Conocimientos sólidos de Junior Backend
✅ Experiencia práctica con Git, Deploy, Testing
✅ API REST profesional con frontend dinámico

### PODRÁS APLICAR A:
✅ Posiciones Junior Backend Developer
✅ Trainee/Intern programs
✅ Freelance projects
✅ Bootcamp instructor assistant
✅ Remote junior positions

### NIVEL ALCANZADO:
**Junior Backend Developer** - Listo para el mercado laboral

---

## 📞 CONTACTO Y SOPORTE:
- Plan creado: 15 julio 2025
- Inicio: 16 julio 2025
- Fin proyectado: 10 septiembre 2025
- Intensidad: 4 horas/día
- Total horas: 224 horas

**¡ÉXITO EN TU TRANSFORMACIÓN A JUNIOR DEVELOPER!** 🚀

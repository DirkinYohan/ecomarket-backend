# EcoMarket Backend

API backend para **EcoMarket**, un caso práctico ficticio de desarrollo de software orientado a la integración de una pasarela de pagos mediante Stripe. El proyecto utiliza Python y FastAPI para exponer servicios REST que permiten iniciar el proceso de pago de los pedidos.

El desarrollo se organiza mediante la metodología Scrum, con seguimiento de tareas en ClickUp y control de versiones en GitHub.

## Objetivos del proyecto

- Desarrollar un endpoint para crear intenciones de pago con Stripe.
- Proporcionar respuestas JSON estandarizadas para la integración con el frontend.
- Gestionar errores relacionados con las solicitudes de pago.
- Integrar el desarrollo backend con una interfaz móvil construida con Flutter.
- Aplicar buenas prácticas de Git, revisión de código y pruebas de calidad.
- Vincular las tareas de desarrollo con commits, ramas y Pull Requests.

## Tecnologías utilizadas

| Tecnología | Propósito |
|---|---|
| Python | Lenguaje de programación del backend |
| FastAPI | Framework para desarrollar la API REST |
| Stripe | Integración con la pasarela de pagos |
| Git y GitHub | Control de versiones y colaboración |
| ClickUp | Gestión del Product Backlog, Sprints y defectos |
| Pytest | Pruebas automatizadas |
| Postman | Pruebas de endpoints HTTP |
| Flutter | Aplicación cliente que consume la API |

## Funcionalidad principal

### Integración con Stripe

La historia de usuario **ECO-101: Integración de Pasarela de Pagos Stripe** contempla la creación de un endpoint que genera una intención de pago mediante Stripe.

**Endpoint**

`POST /api/v1/payments/create-intent`

**Parámetros previstos**

| Parámetro | Tipo | Descripción |
|---|---|---|
| `amount` | Entero | Monto del pago en la unidad mínima de la moneda |
| `currency` | Cadena | Moneda del pago; por defecto, `usd` |

**Ejemplo de solicitud**

```json
{
  "amount": 2500,
  "currency": "usd"
}
```

**Ejemplo de respuesta exitosa**

```json
{
  "client_secret": "pi_example_secret",
  "id": "pi_example"
}
```

Los valores anteriores son ilustrativos y no representan credenciales ni identificadores reales de Stripe.

El `client_secret` permite al cliente continuar el flujo de pago mediante la integración correspondiente de Stripe.

### Validaciones y manejo de errores

La implementación contempla los siguientes criterios:

- Validación de los montos recibidos.
- Rechazo de montos negativos o iguales a cero.
- Manejo de errores durante la creación de la intención de pago.
- Respuestas HTTP apropiadas para solicitudes inválidas.
- Validación de la firma de los webhooks de Stripe, como parte de los criterios de aceptación.

**Nota:** estos puntos describen los requisitos del caso práctico; su cumplimiento depende de la implementación y de las pruebas ejecutadas.

## Estructura propuesta del proyecto

```text
ecomarket-backend/
├── app/
│   ├── main.py
│   └── routers/
│       └── payments.py
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

Esta estructura es una propuesta inicial para organizar el código. Los archivos deben crearse según la implementación real del repositorio.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/DevStudioUCC/ecomarket-backend.git
cd ecomarket-backend
```

### 2. Crear un entorno virtual

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

En Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

Si el proyecto cuenta con un archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Si todavía no existe, las dependencias básicas del ejemplo incluyen:

```bash
pip install fastapi uvicorn stripe
```

### 4. Configurar las variables de entorno

Crear un archivo `.env` local para almacenar las credenciales de Stripe y configurar la aplicación para leerlas desde el entorno.

Ejemplo de `.env.example`:

```dotenv
STRIPE_SECRET_KEY=sk_test_replace_with_your_test_key
```

No subir el archivo `.env` ni las claves secretas al repositorio. Utilizar credenciales de prueba durante el desarrollo.

### 5. Ejecutar la API

Si el punto de entrada de FastAPI es `app/main.py` y la instancia se llama `app`:

```bash
uvicorn app.main:app --reload
```

La dirección local predeterminada será `http://127.0.0.1:8000`.

La documentación interactiva de FastAPI estará disponible en:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Estos comandos presuponen que la aplicación y el enrutador están configurados correctamente.

## Pruebas de calidad

El caso práctico contempla pruebas del endpoint y validación de errores mediante Postman y Pytest.

Escenarios relevantes:

1. Creación de una intención de pago con un monto válido.
2. Rechazo de un monto negativo, por ejemplo, `-500`.
3. Rechazo de un monto igual a cero.
4. Manejo de errores provenientes de Stripe.
5. Verificación de la respuesta JSON y los códigos HTTP.
6. Validación de la firma de los webhooks.

Para ejecutar las pruebas automatizadas, cuando estén implementadas:

```bash
pytest
```

Un objetivo importante del control de calidad es garantizar que las solicitudes inválidas no produzcan errores internos inesperados. Por ejemplo, el escenario ECO-101-B1 requiere que un monto negativo sea rechazado con HTTP `400 Bad Request`, en lugar de generar un HTTP `500 Internal Server Error`.

## Flujo de trabajo con Git y ClickUp

El desarrollo se gestiona mediante tareas identificadas con el prefijo `ECO`.

El flujo de trabajo propuesto es:

1. Crear una historia de usuario en el Product Backlog.
2. Estimar su esfuerzo durante la planificación del Sprint.
3. Crear una rama de trabajo vinculada al identificador de ClickUp.
4. Implementar la funcionalidad y realizar commits descriptivos.
5. Abrir una Pull Request para revisión de código.
6. Integrar los cambios mediante merge.
7. Ejecutar las pruebas de QA y corregir los defectos detectados.
8. Documentar la solución y cerrar la tarea cuando se cumplan los criterios de aceptación.

**Ejemplo de rama backend:**

```bash
git checkout -b feature/ECO-101-stripe-backend
```

**Ejemplo de commit:**

```bash
git add .
git commit -m "feat(payments): ECO-101 crea endpoint para Stripe PaymentIntent"
git push origin feature/ECO-101-stripe-backend
```

El identificador `ECO-101` permite relacionar los cambios de código con la historia de usuario correspondiente en ClickUp.

## Organización del equipo

| Integrante | Responsabilidad |
|---|---|
| Dirkin | Product Owner y definición de historias de usuario |
| Calzada | Scrum Master y seguimiento del Sprint |
| Nicolas | Desarrollo backend e integración con Stripe |
| Martinez | Desarrollo frontend con Flutter |
| Juan Camilo | QA, pruebas de integración y seguimiento de defectos |

## Seguridad

- No almacenar claves secretas directamente en el código fuente.
- Utilizar variables de entorno para configurar credenciales.
- Verificar la firma de los webhooks de Stripe.
- Validar los datos recibidos por la API.
- Revisar los cambios mediante Pull Requests.
- Evitar registrar información sensible de los pagos.
- Utilizar el entorno de pruebas de Stripe antes de cualquier despliegue real.

## Estado del proyecto

Este repositorio corresponde a un **caso práctico ficticio con fines académicos**, centrado en la integración de pagos, la colaboración mediante GitHub y ClickUp y el control de calidad durante un Sprint.

La documentación describe la funcionalidad prevista y el flujo de trabajo del caso. No implica que la API esté desplegada, que todos los requisitos estén implementados o que los pagos se encuentren habilitados en producción.

## Licencia

La licencia del proyecto debe definirse según las condiciones de uso y distribución acordadas por el equipo.

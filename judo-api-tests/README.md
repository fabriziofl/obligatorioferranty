# Judo API Tests

Proyecto mínimo para empezar a testear APIs con **Judo Framework** usando un mock server local.

## Requisitos

- Python 3.10+

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Ejecutar pruebas

```bash
pytest
```

## Qué prueba este ejemplo

El test `tests/test_mock_api.py`:

1. Levanta un mock server con Judo en `localhost:8099`.
2. Define un endpoint `GET /users/1` con respuesta controlada.
3. Ejecuta la petición HTTP y valida estado y contenido JSON.
4. Detiene el mock server al terminar.

Esto te deja una base para agregar más escenarios de API sin depender de servicios externos.

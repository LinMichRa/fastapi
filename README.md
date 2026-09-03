# Despliegue continuo en Render

El proyecto se puede desplegar como un Web Service gratuito en Render usando el `Dockerfile` incluido.

1. Sube este proyecto a GitHub en la rama `main`.
2. En [Render](https://render.com/), crea un **Web Service** y conecta el repositorio de GitHub.
3. Selecciona **Docker** como entorno de ejecucion. Render construira el servicio desde el `Dockerfile` y detectara el puerto `8000` expuesto por la aplicacion.
4. Cuando el servicio haya sido creado, abre **Settings** y copia la URL de **Deploy Hook**.
5. En GitHub, abre **Settings > Secrets and variables > Actions**, crea un secreto nuevo llamado `RENDER_DEPLOY_HOOK` y pega esa URL como valor.
6. Haz push a `main`. El flujo `.github/workflows/deploy-render.yml` se ejecutara y solicitara un nuevo despliegue a Render.

El plan gratuito de Render puede suspender servicios inactivos; la primera solicitud despues de la suspension puede tardar unos segundos.

# Servicio FastAPI de Cédula

Este proyecto expone un endpoint para generar un número aleatorio de 10 dígitos.

## Requisitos

- Docker
- Docker Compose

## Levantar el servicio con Docker Compose

1. Abre una terminal en la raíz del proyecto.
2. Ejecuta:

```bash
docker compose up --build
```

3. Una vez levantado, el servicio quedará disponible en:

```text
http://localhost:8000
```

## Endpoint disponible

### GET /obtenercedula

Genera y devuelve una cédula aleatoria de 10 dígitos.

### Respuesta esperada

```json
{
  "cedula": 6355047539
}
```

## Ejemplo de payload

Como es un endpoint GET, no se envía body en la petición.

### URL de prueba

```text
http://localhost:8000/obtenercedula
```

## Swagger UI

FastAPI incluye documentación automática con Swagger.

Puedes abrir en tu navegador:

```text
http://localhost:8000/docs
```

Allí podrás probar el endpoint visualmente desde la interfaz interactiva de Swagger.

## Postman

Para probarlo en Postman:

1. Abre Postman.
2. Crea una nueva petición `GET`.
3. Coloca la URL:

```text
http://localhost:8000/obtenercedula
```

4. Envía la petición.
5. La respuesta esperada será algo como:

```json
{
  "cedula": 6355047539
}
```

## Docker Compose archivo

```yaml
services:
  api:
    build: .
    container_name: fastapi-cedula
    ports:
      - "8000:8000"
    restart: unless-stopped
```

## Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Notas

- El servicio corre en el puerto `8000`.
- Swagger queda disponible en `/docs`.
- OpenAPI queda disponible en `/openapi.json`.
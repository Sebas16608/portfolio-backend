FROM python:3.13-slim

# Evita .pyc y mejora logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias del sistema para psycopg2
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar y instalar dependencias Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Crear carpeta static si no existe
RUN mkdir -p /app/static

# Collectstatic **usando entorno de Render** (lee variables al run)
# Se recomienda hacerlo al iniciar el contenedor
CMD python manage.py collectstatic --noinput && \
    gunicorn PortFolio.wsgi:application --bind 0.0.0.0:8000

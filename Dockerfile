FROM python:3.13-slim

# Evita archivos .pyc y habilita logs inmediatos
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias necesarias para psycopg2 (postgres)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Recolectar archivos estáticos (si tenés admin o frontend)
# (Lo haremos desde docker-compose)
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "Portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]

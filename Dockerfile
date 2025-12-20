FROM python:3.13-slim

# Evita .pyc y mejora logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias del sistema (psycopg2)
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . .

# Static files
RUN python manage.py collectstatic --noinput

# Puerto (Render usa 8000)
EXPOSE 8000

# Run
CMD ["gunicorn", "PortFolio.wsgi:application", "--bind", "0.0.0.0:8000"]

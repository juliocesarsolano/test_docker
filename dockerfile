# Imagen base ligera con Python
FROM python:3.10-slim

# Evitar que Python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar dependencias del sistema necesarias para MLflow y scikit-learn
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exponer el puerto donde correrá Flask
EXPOSE 8000

# Comando para iniciar la aplicación (puedes cambiar a gunicorn si lo deseas)
CMD ["python", "app.py"]
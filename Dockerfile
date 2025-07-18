# Imagen base de Python optimizada para producción
FROM python:3.10-slim

# Crear directorio de trabajo
WORKDIR /app

# Copiar solo los requirements primero (para aprovechar el cache de Docker)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY ./app ./app

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando por defecto para iniciar el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

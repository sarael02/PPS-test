# Imagen base
FROM python

# Establecer el directorio de trabajo
WORKDIR /app

COPY requirements.txt .

# Instalar las dependencias
# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los archivos de la aplicación al contenedor
COPY ./src /app

# Exponer el puerto utilizado por FastAPI
EXPOSE 8000

# Iniciar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]


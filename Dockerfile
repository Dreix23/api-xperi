# Usa una imagen oficial de Python como imagen padre
FROM python:3.9

# Etiqueta con la información del autor (opcional)
LABEL authors="Dreix"

# Establece el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copia el archivo de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt ./

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente del proyecto
COPY . .

# Informa a Docker que la aplicación escucha en el puerto 8000
EXPOSE 8000

# Define el comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

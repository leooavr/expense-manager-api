# Utiliza una imagen base adecuada para tu proyecto
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al directorio de trabajo
COPY . /app

# Instala las dependencias del proyecto desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecuta tu aplicación
EXPOSE 8000

# Inicia la aplicación cuando se ejecute el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Imagen Base
FROM python:3.9-slim

# Definir nuestro espacio de trabajo
WORKDIR /app

# Copiar las librerias
COPY requirements.txt ./


# Instalar las librerias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el codigo
COPY . .

# expose 
EXPOSE 5000

CMD ["python", "app.py"]


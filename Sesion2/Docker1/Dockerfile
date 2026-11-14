# Definir una imagen Base
FROM python:3.9-slim

# Actualizar el sistema e instalar paquetes.
# Instalando liberira pip y notebook
RUN pip3 install --upgrade pip && \
    pip3 install notebook==6.5.6

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /workspace

# Almacenar los archivos del configuracion de Jupyter Notebook
RUN mkdir -p /root/.jupyter

# Se agregan las configuraciones basicas de Jupyter Notebook
# Dehsabilitar la autenticacion por token y contraseña
# Evitar que se abra el navegador automaticamente al iniciar Jupyter Notebook
# Permitir que Jupyter Notebook se ejecute como root dentro del contenedor
RUN echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /root/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> /root/.jupyter/jupyter_notebook_config.py

# Exponer el puerto del servidor de Jupyter Notebook
EXPOSE 8888

# Comando pro defecto
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]







    

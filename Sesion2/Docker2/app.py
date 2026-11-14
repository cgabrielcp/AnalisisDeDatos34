from flask import Flask

# Crear la instania o ruta Flask
app = Flask(__name__)


# Rutas de la aplicación Flask ( Servicio )
@app.route('/api/hello')
def hello ():
    '''
        Get Hello
        Retorna un simple mensaje de conexion

    '''
    return "Hola Mundo desde Docker - API!"

@app.route('/api/getData')
def getData ():
    '''
        get Data
        Retorna un dato particular

    '''
    resultado = ' Data Obtenida'
    return resultado


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



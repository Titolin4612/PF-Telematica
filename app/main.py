# ---------------------------
# Autor: Santiago Hernandez Morantes
# Proyecto: Servicio Telemático 
# Framework: Flask (Python)
# ---------------------------

from flask import Flask, render_template

# Instanciar la aplicación Flask
app = Flask(__name__)

# Ruta principal de la app
@app.route('/')
def inicio():
    # Renderiza el archivo HTML ubicado en templates/index.html
    return render_template('index.html')

# Ejecutar el servidor web Flask
if __name__ == '__main__':
    # 0.0.0.0 permite acceder desde fuera del contenedor
    app.run(host='0.0.0.0', port=80)

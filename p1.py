from flask import Flask, request, jsonify

app = Flask(_name_)

# Lista en memoria para almacenar productos
productos = []

@app.route('/productos', methods=['POST'])
def agregar_producto():
    nuevo_producto = request.get_json()
    if not nuevo_producto or 'nombre' not in nuevo_producto:
        return jsonify({'error': 'El producto debe tener un nombre'}), 400
    productos.append(nuevo_producto)
    return jsonify({'mensaje': 'Producto agregado', 'producto': nuevo_producto}), 201

@app.route('/productos', methods=['GET'])
def listar_productos():
    return jsonify({'productos': productos})

if _name_ == '_main_':
    app.run(debug=True)

# Comentario final:
# Esta implementación es monolítica porque toda la lógica (rutas, lógica de negocio y almacenamiento de datos) está contenida en un solo archivo y en un solo servicio.
# Las desventajas de esta estructura son:
# - Difícil de escalar: no se pueden separar fácilmente las distintas partes (por ejemplo, la base de datos o las rutas) en microservicios o módulos independientes.
# - Mantenimiento complicado: a medida que la aplicación crece, este archivo se vuelve muy grande y difícil de gestionar.
# - Reutilización limitada: no se puede reutilizar fácilmente la lógica de negocio en otros contextos sin duplicarla.
# - No apto para producción: guardar datos en memoria no es persistente; si el servidor se reinicia, todos los productos se pierden.

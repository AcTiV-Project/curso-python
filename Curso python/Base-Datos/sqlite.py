#Importar modulo
import sqlite3


#Conexion
conexion = sqlite3.connect('pruebas.db')

#Crear Cursor
cursor = conexion.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"+
    "titulo varchar(255),"+
    "descripcion text,"+
    "precio int(255)"+
")")

#Guardar cambios
conexion.commit()

#Insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer productos', 'Descripcion del productos', 24)")
conexion.commit()

#Borrar datos
cursor.execute("DELETE FROM productos")


#Listar datos
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

print(productos)

#Cerrar conexion
conexion.close()

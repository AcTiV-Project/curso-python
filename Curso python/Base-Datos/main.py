import mysql.connector

#Conexion

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)


#Creando una base de datos
cursor = database.cursor(buffered=True)

#cursor.execute("CREATE DATABASE master_python")

#Creando tablas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculos PRIMARY KEY(id)
    )
""")

#Insertar registros
cursor.execute("INSERT INTO vehiculos VALUES(null, 'Kia', 'Rio', 10995)")
database.commit()


#Consulta SQL
cursor.execute("SELECT * FROM vehiculos")
resultado = cursor.fetchall()

for coche in resultado:
    print(coche)


#Borrar registros de la tabla
cursor.execute("DELETE FROM vehiculos WHERE modelo = 'Rio' ")
database.commit()

#Actualizar registros
cursor.execute("UPDATE vehiculos SET precio=30000 WHERE marca='Kia'")
database.commit()

print(cursor.rowcount, "Actualizados")
import psycopg2

#reaizar conexión a la base de Datos

conexion = psycopg2.connect(
    host = "localhost", 
    port = "5432",
    database = "credenciales",
    user = "Admin",
    password = "p4ssw0rdDB"
)

#crear cursos
cursor = conexion.cursor()

#ejecuta la consulta
cursor.execute ("SELECT *  FROM usuarrios")

registros = cursor.fechall()

for fila in registros:
    print (fila)

cursor.close()
conexion.close()
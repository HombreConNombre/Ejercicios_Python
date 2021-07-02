import sqlite3

conexion=sqlite3.connect("ejemplo.db")
cursor= conexion.cursor()
'''
cursor.execute("""create table clientes (
    DNI VARCHAR(9) PRIMARY KEY,
    nombre VARCHAR(100),
    edad INTEGER,
    CORREO VARCHAR(100))"""
    )
'''
#cursor.execute("SELECT * FROM clientes")

#cliente=cursor.fetchone() #Muestra la línea, si se vuelve a ejecutar saldría la siguiente

#print(cliente[0]," ",cliente[1]," ",cliente[2])

#Introducir varios registros en la BBDD

usuarios=[
    ("99977653C","Mario",30,"mariocorreo@correo.com"),
    ("94333653F","Lucia",25,"lucia@correo.com"),
    ("99343653Z","Alejandra",32,"alejandra@correo.com")
]

cursor.executemany("INSERT INTO clientes VALUES (?,?,?,?)",usuarios)

#cursor.execute("INSERT INTO clientes VALUES('ADRIAN',20,'adriancorreo@correo.com')")



conexion.commit()

conexion.close()
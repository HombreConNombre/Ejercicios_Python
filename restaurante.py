import sqlite3

#Primera parte del ejercicio. La segunda se encuentra en menu.py

salir=False



def crearBD():

    try:
        conexion=sqlite3.connect("restaurante.db")
        cursor=conexion.cursor()
        cursor.execute("""CREATE TABLE categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL
        )""")
        cursor.execute("""CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id)
        )""")
        conexion.commit()
        conexion.close()
    except:
        print("ERROR al crear las tablas")

def agregar_categoria():
    try:
        conexion=sqlite3.connect("restaurante.db")
        cursor=conexion.cursor()
        nombreCategoria=input("Introduce el nombre de la categoria: ")
        cursor.execute("""INSERT INTO categoria VALUES (null,'{}')
        """.format(nombreCategoria))
        conexion.commit()
        conexion.close()
    except sqlite3.IntegrityError:
        print("ERROR AL INTRODUCIR LA CATEGORIA")
    else:
        print("Se ha introducido correctamente\n")

def agregar_plato():
    try:
        listaNombres=[]
        listaIDs=[]
        conexion=sqlite3.connect("restaurante.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM categoria")
        categorias=cursor.fetchall()
        for categoria in categorias:
            print(categoria[1])
            listaNombres.append(categoria[1])
            listaIDs.append(categoria[0])
        opcion=input("Elige en qué categoria vas a meter el plato: ")
        IDTemp=listaIDs[listaNombres.index(opcion)]
        if IDTemp>=0 and IDTemp<=len(listaIDs)-1:
            nombrePlato=input("Introduce el nombre del plato: ")
            cursor.execute("INSERT INTO plato VALUES (null,'{}',{})".format(nombrePlato,IDTemp))
        conexion.commit()
        conexion.close()
    except:
        print("ERROR AL AGREGAR EL PLATO")

def mostrar_menu():
    try:
        conexion=sqlite3.connect("restaurante.db")
        cursor=conexion.cursor()
        cursor.execute("SELECT * FROM plato ORDER BY categoria_id")
        platos=cursor.fetchall()
        nombresPrimeros=""
        nombresSegundos=""
        nombresPostres=""
        for plato in platos:
            if plato[2]==0:
                nombresPrimeros=nombresPrimeros+"\n\t\t"+plato[1]
            elif plato[2]==1:
                nombresSegundos=nombresSegundos+"\n\t\t"+plato[1]
            else :
                nombresPostres=nombresPostres+"\n\t\t"+plato[1]
        print('''
            *------------*MENU*------------*
            PRIMEROS PLATOS
            {}
            
            SEGUNDOS PLATOS
            {}
            
            POSTRES
            {}
        '''.format(nombresPrimeros,nombresSegundos,nombresPostres))
    except:
        print("Error al mostrar el menú")

while salir==False:
    opcion=int(input("""Elige una de las siguientes opciones:
    0.- Crear las tablas SOLO ADMINISTRADORES
    1.- Agregar categoria
    2.- Agregar plato
    3.- Mostrar menu
    INTRODUCE CUALQUIER OTRO VALOR PARA SALIR DEL PROGRAMA.
    """))
    if opcion==0:
        crearBD()
    elif opcion==1:
        agregar_categoria()
    elif opcion==2:
        agregar_plato()
    elif opcion==3:
        mostrar_menu()
    else:
        salir=True


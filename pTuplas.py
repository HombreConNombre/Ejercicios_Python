#Ejercicio 1 TUPLA (La comento para que no se active en las pruebas) 
'''
tupla=(1,2,6,78,"Hola",2,2,2,2,2,2,2)
print(tupla.count(2),"y Hola aparece en la posicion: ", tupla.index("Hola"))
'''
#Ejercicio 2 CONJUNTO (La comento para que no se active en las pruebas)
'''
grupo={"Miguel","Blanca","Mario","Andrés"}
grupo.add("Ana")
grupo.add("Ramón")
grupo.add("Eric")
grupo.add("Marta")
grupo.add("David")
print(grupo)
grupo.remove("Mario")
grupo.remove("Miguel")
grupo.remove("Ramón")
print(grupo)
'''
#Ejercicio 3 DICCIONARIOS (La comento para que no se active en las pruebas)
'''
animales={"caballo":"","vaca":""}
animales["perro"]="dog"
animales["gato"]="cat"
animales["rana"]="frog"

animales["caballo"]="horse"
animales["vaca"]="cow"

del(animales["rana"])
del(animales["vaca"])
print(animales)
'''
#Ejercicio 4 USUARIOS (La comento para que no se active en las pruebas)
'''
usuarios={"Marta","David","Elvira","Juan","Marcos"}
adminis={"Juan","Marta"}
adminis.remove("Juan")
adminis.add("Marcos")

for usuario in usuarios:
    if adminis.__contains__(usuario):
        print(usuario," tiene permisos de administrador")
    else:
        print(usuario," no tiene permisos")
'''
#Ejercicio 5 HOJA DE PERSONAJES  (La comento para que no se active en las pruebas)
'''
caballero={"vida":2,"ataque":2,"defensa":2,"alcance":2}
arquero={"vida":2,"ataque":2,"defensa":2,"alcance":2}
guerrero={"vida":2,"ataque":2,"defensa":2,"alcance":2}

caballero["vida"]=guerrero["vida"]*2
caballero["defensa"]=guerrero["defensa"]*2

guerrero["ataque"]=caballero["ataque"]*2
guerrero["alcance"]=caballero["alcance"]*2

arquero["vida"]=guerrero["vida"]
arquero["ataque"]=guerrero["ataque"]
arquero["defensa"]=guerrero["defensa"]/2
arquero["alcance"]=guerrero["alcance"]*2

print("Caballero: ",caballero)
print("Arquero: ",arquero)
print("Guerrero: ",guerrero)
'''
#Ejercicio 6 ORDENACIÓN Y COLA
tareas=[
    [6,"Distribución"],
    [2,"Diseño"],
    [1,"Concepción"],
    [7,"Mantenimiento"],
    [4,"Producción"],
    [3,"Planificación"],
    [5,"Pruebas"]
]
from collections import deque

tareas.sort()
cola=deque()
for tarea in tareas:
    cola.append(tarea[1])

print(cola)
#Ejercicio 1 Flujo y conversiones (La comento para que no se active en las pruebas)
'''
multiples=[]
numero=-1
while numero<0 or numero>9:
    numero=int(input("Introduce un número entre 0 y 9:"))
multiples=list(range(0,101,numero))
print(multiples)
'''
#Ejercicio 2 (La comento para que no se active en las pruebas)
'''
Comentario multiple linea

n1=int(input("Introduce el primer valor: "))
n2=int(input("Introduce el segundo valor: "))
while True:
    opcion=int(input("""Introduce qué quieres hacer
    1-> suma los números
    2-> resta los números
    3-> multiplica los números
    4-> salir
     """))
    if opcion==1:
        print(n1+n2)
    elif opcion==2:
        print(n1-n2)
    elif opcion==3:
        print(n1*n2)
    elif opcion==4:
        break
    else:
        print("La opción no es correcta")
'''
#Ejercicio 3 (La comento para que no se active en las pruebas)
'''
while True:
    n=int(input("Introduce un número impar para acabar el programa: "))
    if n%2!=0:
        break
'''
#Ejercicio 4 (La comento para que no se active en las pruebas)
'''
pares=list(range(0,11,2))
sumatorio=0
for x in pares:
    sumatorio+=x
print(sumatorio)
'''
#Ejercicio 5 (La comento para que no se active en las pruebas)
'''
opcion=-1
acumulado=0
nveces=0
while opcion!=0:
    opcion=int(input("Introduce un numero: "))
    if opcion!=0:
        acumulado+=opcion
        nveces+=1
media=acumulado/nveces
print(media)
'''
#Ejercicio 6 
list1=['H','o','l','a','','m','u','n','d','o']
list2=['H','o','l','a','','m','u','n','d','o']
list3=[]
for x in list1:
    if x in list2 and x not in list3:
        list3.append(x)
print(list3)

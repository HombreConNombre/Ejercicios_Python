#Ejercicio 1 Excepcion base
'''
try:
    n1=int(input("Introduce un número: "))
    n2=int(input("Introduce el segundo número: "))
    print(n1/n2)
except ZeroDivisionError:
    print("El número que has introduce en el segundo bloque es 0. Recuerda que no se puede dividir entre 0.")
'''
#Ejercicio 2 Excepción completa
while True:
    try:
        colores={"rojo":"red","blanco":"white","morado":"purple"}
        clave=input("Introduce la palabra para buscar en el diccionario: ")
        print(colores[clave])
        break
    except KeyError:
        print("La palabra que has introducido no existe. Prueba otra vez. Las palabras que hay son:",colores)
    else:
        print("Gracias por utilizar correctamente el programa")
        break
    finally:
        print("Vaya, existo :3")  

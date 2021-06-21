import sys, math
#Ejercicio 1 Script Tabla (Lo comento para no se ejecute)
'''
if len(sys.argv)!=3:
    print("Este script requiere la introdución de dos varibles")
    print("La primera para las filas y la segunda para las variables. Números enteros, por favor.")
else :
    filas=int(sys.argv[1])
    columnas=int(sys.argv[2])
    for f in range(filas):
        for c in range(columnas):
            print("*",end="") #La propiedad 'end' sirve para determinar el fin y decidir si hay salto de línea o no.
        print("*")
'''
#Ejercicio 2 Script Descompositor
if len(sys.argv)==2:
    n=sys.argv[1]
    print("El programa está descomponiendo tu número")
    longitud=len(n)
    for x in range(longitud):
        valorResultado=n[x]
        print("{:04d}".format(int(float(valorResultado)*math.pow(10,longitud-x-1))))
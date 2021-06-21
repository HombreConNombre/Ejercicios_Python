#Ejercicio 1 Recortar números (Lo comento para que no se active)
'''
def recortar(numero,minimo,maximo):
    if minimo>maximo:
        maximoAUX=maximo
        maximo=minimo
        minimo=maximoAUX
    if minimo<numero:
        return minimo
    elif maximo>numero:
        return maximo
    else:
        return numero
print(recortar(5,10,1))
'''
#Explicación 1 Argumentos indeterminados[DOS PARTES: 1/2]
'''
def indeterminados_lista(*args): #Esto recibe una tupla args
    print(args)
'''
'''
def indeterminados_nombres(**kwargs): #Esto recibe un diccionario
    for arg,argValue in kwargs: 
        print(arg," ",argValue)
'''
#Ejercicio 2 Argumentos indeterminados
'''
def indeterminados(*args,**kwargs):
    sumatorio=0
    for n in args:
        sumatorio+=n
    for args in kwargs:
        print(args,"  ",kwargs[args])
    print(sumatorio)

indeterminados(4,5,6,7,8,c="Valor",n=5676)
'''
#Ejercicio 3 Recursividad

def sumatorio(numero):
    if numero>0:
        numero+=sumatorio(numero-1)
    return numero

print(sumatorio(3))

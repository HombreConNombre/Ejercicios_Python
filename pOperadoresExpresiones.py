#Ejercicio 1 (La comento para que no se active en las pruebas)
'''
expresiones=[False==True,10>=2*4,33/3==11,True>False,True*5==2.5*2]
print(expresiones)

resultado=[]
for x in expresiones:
    respuesta=expresiones[x]
    resultado.append(respuesta)
print(expresiones==resultado)
'''
#Ejercicio 2 (La comento para que no se active en las pruebas)
'''
expresion=False
edad=11
nombre="****"
nombre=str(nombre)
if nombre!="****" and edad>10 and edad<18 and len(nombre)>=3 and len(nombre)<10:
    expresion=True

print(expresion)
'''
#Ejercicio 3 

n1=int(input("Introduce un número:"))
n2=int(input("Introduce otro número:"))
print(n1==n2,n1!=n2,n1>n2,n2<=n1)

texto="Hola, me llamo Nombre y estoy estudiando"
print(len(texto)>=3 and len(texto)<10, len(texto))

n_magic=12345679
n_usu=0
while n_usu<1 or n_usu>9:
    n_usu=int(input("Introduce un número del 1 al 9: "))
n_usu*=9
n_magic*=n_usu
print(n_magic)
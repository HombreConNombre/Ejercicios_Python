import io, pathlib, pickle,csv, json
#Bloque lectura de TXT y de Pickle(lectura y escritura binaria no directa, utilizando la librería pickle)
'''
#nombreArchivo="fichero_de_texto.txt"   Linea para ficheros de texto normal
nombreArchivo="fichero.pckl"
objetoArchivo=pathlib.Path(nombreArchivo)

lista=[1,2,4,7,8,9,12,23]

if objetoArchivo.is_file():
    fichero = io.open(nombreArchivo,"a")
else:
    fichero = io.open(nombreArchivo,"wb") #w=escritura normal wb=escritura binaria (recuerda que write=borrar lo que hay en el archivo)
    
    textoIncluir="abc def ghi jkl mno pqrs tuv wxyz ABC DEF GHI JKL MNO PQRS TUV WXYZ !§ $%& /() =?* <> #|; ²³~ @`´ ©«» ¤¼× { abc def ghi jkl mno pqrs tuv wxyz ABC DEF GHI JKL MNO PQRS TUV WXYZ !§ $%& /() =?* <> #|; ²³~ @`´ ©«» ¤¼× {} abc def ghi jkl mno pqrs tuv wxyz ABC DEF GHI JKL MNO PQRS TUV WXYZ !§ $%& /() =?* '<> #|; ²³~ @`´ ©«» ¤¼× } abc def ghi jkl mno pqrs tuv wxyz ABC DEF GHI JKL MNO PQRS TUV WXYZ !§ $%& /() =?* '<> #|; ²³~ @`´ ©«» ¤¼× } abc def ghi jkl mno pqrs tuv wxyz ABC DEF GHI JKL MNO PQRS TUV WXYZ !§ $%& /() =?* '<> #|; ²³~ @`´ ©«» ¤¼× { abc def ghi jkl mno pqrs tuv wxyz ABC DEF GHI JKL MNO PQRS TUV WXYZ !§ $%& /() =?* '<> #|; ²³~ @`´ ©«» ¤¼× } abc def ghi jkl mno pqrs tuv wxyz ABC DEF GHI JKL MNO PQRS TUV WXYZ !§ $%& /() =?* '<> #|; ²³~ @`´ ©«» ¤¼× }abc def ghi jkl mno pqrs tuv wxyz ABC DEF GHI"
    fichero.write(textoIncluir) 
    #Este comentario es para ficheros normales
    pickle.dump(lista,fichero)

    fichero.close()
    del(fichero)

fichero=open(nombreArchivo,"rb")
fichero.seek(0)#nos colocamos al inicio del archivo(en este momento no haría falta pero para recordar el comando)
contenidoFichero=pickle.load(fichero)
print(contenidoFichero)

#RECUERDA QUE HAY COSAS DE PICKLE Y OTRAS DE FICHEROS TXT
contenidoFichero=fichero.readlines()

for contenedorTexto in contenidoFichero: #Lectura por filas
    print(contenedorTexto)

print(fichero.read()) #Lectura general
'''
#Bloque CSV
'''
contactos=[
    ("Manuel","Gestor","manuelcontacto@correo.com"),
    ("Adrian","Programador","adriancontacto@correo.com"),
    ("Ana","Médico","anacontacto@correo.com")
]
with open("contactos.csv","w",newline="\n") as csvfile:
    escritura = csv.writer(csvfile, delimiter=",")
    for contacto in contactos:
        escritura.writerow(contacto)

with open("contactos.csv",newline="\n") as csvfile:
    lectura = csv.reader(csvfile, delimiter=",")
    for contacto in lectura:
        print(contacto)
'''
#Bloque JSON
contactos=[
    ("Manuel","Gestor","manuelcontacto@correo.com"),
    ("Adrian","Programador","adriancontacto@correo.com"),
    ("Ana","Médico","anacontacto@correo.com")
]
datos=[]
for nombre,puesto,correo in contactos:
    datos.append({"nombre":nombre,"puesto":puesto,"correo":correo})

with open("contactos.json","w") as jsonfile:
    json.dump(datos,jsonfile)

datos=None

with open("contactos.json") as jsonfile:
    datos=json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"],contacto["puesto"],contacto["correo"])

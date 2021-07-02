from tkinter import *
'''
def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
    
def resetear():
    opcion.set(None)
    monitor.config(text="")

'''
'''
def lecheOAzucar():
    respuesta=""
    if leche.get()==0:
        respuesta+="sin leche "
    else :
        respuesta+="con leche "
    if azucar.get()==0:
        respuesta+="y sin azucar"
    else:
        respuesta+="y con azucar"
    respuestaLabel.config(text=respuesta)

'''
root=Tk()
'''
root.title("Primer programa")
root.iconbitmap("img/avion.ico")



frame=Frame(root)
frame.pack(side="top" ,anchor="w")
frame.config(width=500 , height=350)
frame.config(cursor="arrow")
frame.config(bg="lightyellow")
frame.config(relief="ridge")

label=Label(root, text="¡Hola mundo!")
label.place(x=100,y=100)

nombreLabel=Label(root,text="Nombre: ")
nombreLabel.grid(row=0,column=0) #Posicionamiento, como se hacía antiguamente en HTML con tablas

nombreEntrada=Entry(root)
nombreEntrada.grid(row=0,column=1)

passLabel=Label(root,text="Contraseña")
passLabel.grid(row=2, column=0)             #Formulario básico (relleno de texto TextBox)

passwordEntrada=Entry(root)
passwordEntrada.grid(row=2,column=1)
passwordEntrada.config(show="*")

opcion=IntVar()

Radiobutton(root,text="opcion 1", variable=opcion,value=1, command=seleccionar).pack()
Radiobutton(root,text="opcion 2", variable=opcion,value=2, command=seleccionar).pack()
Radiobutton(root,text="opcion 3", variable=opcion,value=3, command=seleccionar).pack()    #RadioButtons

monitor=Label(root)               
monitor.pack()

Button(root, text="Resetear",command=resetear).pack()


leche=IntVar() #0=no 1=sí
azucar=IntVar() #0=no 1=sí

imagen =PhotoImage(file="img/avion.png")
Label(root,image=imagen).pack(side="left")

frame=Frame(root)
frame.pack(side="left")                       #CheckBoxes

Label(frame,text="¿Cómo quieres el café?").pack(anchor="w")
Checkbutton(frame,text="¿Quieres con leche?", variable=leche, onvalue=1,offvalue=0, command=lecheOAzucar).pack()
Checkbutton(frame,text="¿Quieres azucar?",variable=azucar, onvalue=1,offvalue=0, command=lecheOAzucar).pack()

respuestaLabel=Label(frame)
respuestaLabel.pack()
'''

menubar=Menu(root)
root.config(menu=menubar)

fileMenu=Menu(menubar, tearoff=0)#Menu Archivo
fileMenu.add_command(label="Nuevo")
fileMenu.add_command(label="Abrir")
fileMenu.add_command(label="Cerrar")
fileMenu.add_command(label="Guardar")
fileMenu.add_command(label="Guardar Como...")
fileMenu.add_separator()
editMenu=Menu(menubar, tearoff=0)#Menu Editar
helpMenu=Menu(menubar, tearoff=0)#Menu Ayuda


menubar.add_cascade(label="Archivo",menu=fileMenu)
menubar.add_cascade(label="Editar",menu=editMenu)
menubar.add_cascade(label="Ayuda",menu=helpMenu)


root.mainloop()
root.destroy()
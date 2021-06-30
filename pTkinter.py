from tkinter import *

root=Tk()

root.title("Primer programa")
root.iconbitmap("img/avion.ico")
'''
frame=Frame(root)
frame.pack(side="top" ,anchor="w")
frame.config(width=500 , height=350)
frame.config(cursor="arrow")
frame.config(bg="lightyellow")
frame.config(relief="ridge")
'''
label=Label(root, text="¡Hola mundo!")
label.place(x=100,y=100)

nombreLabel=Label(root,text="Nombre: ")
nombreLabel.grid(row=0,column=0) #Posicionamiento, como se hacía antiguamente en HTML con tablas

nombreEntrada=Entry(root)
nombreEntrada.grid(row=0,column=1)

passLabel=Label(root,text="Contraseña")
passLabel.grid(row=2, column=0)

passwordEntrada=Entry(root)
passwordEntrada.grid(row=2,column=1)
passwordEntrada.config(show="*")

root.mainloop()
root.destroy()
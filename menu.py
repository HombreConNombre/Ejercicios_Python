from tkinter import *
import sqlite3

root=Tk()
#Creación de la parte principal

root.title("Restaurante Martínez")
root.resizable(0,0)
root.config(bd=25,relief="sunken")

Label(root,text="Restaurante Martínez",fg="Darkgreen",font=("Times New Roman",28,"bold")).pack()
Label(root,text="MENU COMIDAS",fg="Darkgreen",font=("Times New Roman",28,"bold")).pack()


#Parte de dibujado dinámico del menú
conexion=sqlite3.connect("restaurante.db")
cursor=conexion.cursor()

cursor.execute("SELECT * FROM plato ORDER BY categoria_id")
platos=cursor.fetchall()
idCategoriaTemp=-1
for plato in platos:
    if idCategoriaTemp != plato[2]:
        idCategoriaTemp=plato[2]
        if plato[2]==0:
            Label(root,text="PRIMEROS",font=("Times New Roman",20,"bold")).pack()
        elif plato[2]==1:
            Label(root,text="SEGUNDOS",font=("Times New Roman",20,"bold")).pack()
        elif plato[2]==2:
            Label(root,text="POSTRES",font=("Times New Roman",20,"bold")).pack()
    Label(root,text="{}".format(plato[1]),font=("Times New Roman",16,"bold")).pack()
conexion.close()


root.mainloop()
root.destroy()
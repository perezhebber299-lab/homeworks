import tkinter as tk
from Backend import *
from tkinter import messagebox


#actualiza el texto -----------------
ven1=tk.Tk()
ven1.title("Mi primera aplicacion con Tkinter")

#tamaño de ventana---------------
ven1.geometry("400x300")

etiqueta1=tk.Label(ven1,text="Nombre:")
etiqueta1.pack(pady=10)
entrada1=tk.Entry(ven1,width=30)
entrada1.pack(pady=10)

etiqueta2=tk.Label(ven1,text="Edad:")
etiqueta2.pack(pady=10)
entrada2=tk.Entry(ven1,width=30)
entrada2.pack(pady=10)

etiqueta3=tk.Label(ven1,text="Comida Favorita:")
etiqueta3.pack(pady=10)
entrada3=tk.Entry(ven1,width=30)
entrada3.pack(pady=10)

def registrar():
    name = entrada1.get()
    age = entrada2.get()
    food = entrada3.get()
    
    nuevo_usuario = Usuarios(name, age, food)
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    entrada3.delete(0, tk.END)
    messagebox.showinfo("Registro Exitoso", f"Usuario {name} registrado correctamente.")
    
    
#boton------------------------

boton = tk.Button(ven1, text="registrar")
boton.pack(pady=20)
#etiqueta 

def mostrar_usuarios():
    lista= Usuarios.mostrar_usuarios()
    messagebox.showinfo("Lista de usuarios", lista)


#crear un boton 

boton2 = tk.Button(ven1, text="Mostrar Usuarios")
boton2.pack(pady=10)

#buclu principal de la apñicacion/ventana 

ven1.mainloop()

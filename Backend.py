import csv

class Usuarios():
    lista = []
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food
        if self not in Usuarios.lista:
            Usuarios.lista.append(self)
            
    def mostrar_informacion(self):
        print(f"Nombre: {self.name}, Edad: {self.age}, Comida Favorita: {self.food}")
        
    @classmethod
    def mostrar_usuarios(cls):
        return cls.lista
    
    @classmethod
    def guardar_usuarios(cls):
        campos=["Nombre", "Edad"]
        with open("persona.cvs", "w",encoding="utf-8") as f:
            escritor=csv.DicWriter(f, fieldnames=campos)
            escritor.writeheader()
            for u in cls.lista:
                escritor.writerow({"Nombre": u.name, "Edad": u.age})
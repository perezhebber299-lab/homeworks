from Backend import *

usuario1 = Usuarios("Juan", 23, "Boneless")
usuario2 = Usuarios("Maria", 30, "Pizza")
usuario3 = Usuarios("Carlos", 28, "Sushi")

print (usuario1.mostrar_informacion())
print (usuario2.mostrar_informacion())
print (usuario3.mostrar_informacion())

print (Usuarios.mostrar_usuarios())

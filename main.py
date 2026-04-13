from models import (Pelicula, Clientes, Funcion, Sala)

print("========Cartelera========")
peli1 = Pelicula("El Padrino", 70, "Drama", "3:30")
peli2 = Pelicula("Cars 2", 70, "animacion", "1:30")
peli3 = Pelicula("Terrifer", 75, "Terror", "1:45")
peli4 = Pelicula("El parino 2", 90, "Drama", "4:00")
peli5 = Pelicula("EL hombre araña", 70, "Accion", "2:30")
peli6 = Pelicula("Iron man", 70, "Accion", "1:30")
peli7 = Pelicula("Grandes heroes", 75, "Animacion", "1:20")
peli8 = Pelicula("chuki", 75, "Terror", "1:20")
peli9 = Pelicula("Son como niños", 75, "Comedia", "1:20")
peli10 = Pelicula("El conjuro", 75, "Terror", "1:20")
for p in [peli1, peli2, peli3, peli4, peli5, peli6, peli7, peli8, peli9, peli10]:
    print(p)
    
print("========INFORMACION DE LOS CLIENTES==========")
cli1 = Clientes("Juan", "El Padrino", 2, "3:30")
cli2 = Clientes("Maria", "Cars 2", 4, "1:30")
cli3 = Clientes("Pedro", "Terrifer", 1, "1:45")
cli4 = Clientes("Ana", "El parino 2", 3, "4:00")
cli5 = Clientes("Luis", "EL hombre araña", 2, "2:30")
cli6 = Clientes("Sofia", "Iron man", 1, "1:30")
cli7 = Clientes("Carlos", "Grandes heroes", 5, "1:20")
cli8 = Clientes("Lucia", "chuki", 2, "1:20")
cli9 = Clientes("Diego", "Son como niños", 3, "1:20")
cli10 = Clientes("Marta", "El conjuro", 1, "1:20")
for c in [cli1, cli2, cli3, cli4, cli5, cli6, cli7, cli8, cli9, cli10]:
    print(c)
    


print("--- REGISTRO DE FUNCIONES")
f1  = Funcion(1,  "El padrino", "16:00 hrs", 70)
f2  = Funcion(2,  "Terrifer",  "18:30 hrs", 70)
f3  = Funcion(3,  "Cars 2",  "11:00 hrs", 75)
f4  = Funcion(4,  "chuki",  "20:00 hrs", 75)
f5  = Funcion(5,  "Grandes heroes", "14:00 hrs", 75)
f6  = Funcion(6,  "El conjuro",   "17:00 hrs", 75)
f7  = Funcion(7,  "Son como niños", "21:30 hrs", 75)
f8  = Funcion(8,  "Son como niños",  "10:00 hrs", 75)
f9  = Funcion(9,  "Cars 2", "22:00 hrs", 70)
f10 = Funcion(10, "El conjuro", "19:00 hrs", 70)

for f in [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]:
    print(f.mostrar_detalle())

print("\n---aplicar_descuento ---")
print(f1.aplicar_descuento(20))
print(f5.aplicar_descuento(50))

print("--- REGISTRO DE SALAS ---")
s1  = Sala(1, "Sala 01", 120, "Normal")
s2  = Sala(2, "Sala 02", 100, "Normal")
s3  = Sala(3,  "Sala 03", 80, "3D")
s4  = Sala(4,  "Sala 04", 60,  "IMAX")
s5  = Sala(5, "Sala 05", 90, "4DX")
s6  = Sala(6,  "Sala 06", 110, "Normal")
s7  = Sala(7, "Sala 07", 75,  "3D")
s8  = Sala(8,  "Sala 08", 50, "VIP")
s9  = Sala(9, "Sala 09", 130, "Normal")
s10 = Sala(10, "Sala 10", 65, "IMAX")

for s in [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]:
    print(s.mostrar_detalle())

print("\n---ocupar_asiento / asientos_disponibles ---")
print(s4.ocupar_asiento("A1"))
print(s4.ocupar_asiento("A2"))
print(s4.ocupar_asiento("A1"))  # Ya ocupado
print(s4.asientos_disponibles())

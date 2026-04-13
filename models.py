class Pelicula():
    def __init__(self, pelicula, precio, genero, duracion):
        self.pelicula = pelicula
        self.precio = precio
        self.genero = genero
        self.duracion = duracion
        
    def __str__(self):
        return f'Pelicula: {self.pelicula}, Precio: {self.precio}, Genero: {self.genero}, Duracion: {self.duracion}'    
    
class Clientes():
    def __init__(self, nombre, funcion, cantidad_entradas, duracion):
        self.nombre = nombre
        self.funcion = funcion
        self.cantidad_entradas = cantidad_entradas
        self.duracion = duracion 
    def __str__(self):
        return f'Nombre del cliente: {self.nombre}, funcion: {self.funcion}, numero de entradas: {self.cantidad_entradas}, duracion de la funcion: {self.duracion}'

class Funcion:
    def __init__(self, id_funcion, pelicula, horario, precio_base):
        self.id_funcion = id_funcion
        self.pelicula = pelicula
        self.horario = horario
        self.precio_base = precio_base

    def mostrar_detalle(self):
        return f"ID: {self.id_funcion} | {self.pelicula} | {self.horario} | ${self.precio_base:.2f}"

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio_base * (porcentaje / 100)
        precio_final = self.precio_base - descuento
        return f"Precio final: ${precio_final:.2f} (Ahorraste ${descuento:.2f})"
    
class Sala:
    def __init__(self, id_sala, nombre, capacidad, tipo):
        self.id_sala = id_sala
        self.nombre = nombre
        self.capacidad = capacidad
        self.tipo = tipo
        self.asientos_ocupados = []

    def mostrar_detalle(self):
        return f"ID: {self.id_sala} | {self.nombre} | Capacidad: {self.capacidad} | Tipo: {self.tipo}"

    def ocupar_asiento(self, asiento):
        if asiento in self.asientos_ocupados:
            return f"[ERROR]: El asiento {asiento} ya está ocupado."
        self.asientos_ocupados.append(asiento)
        return f"[OK]: Asiento {asiento} ocupado."

    def asientos_disponibles(self):
        return f"Ocupados: {self.asientos_ocupados}"
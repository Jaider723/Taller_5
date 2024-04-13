import os

class Vehiculo:
    def __init__(self, marca, modelo, color, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
        self.kilometraje = kilometraje

    def mostrar_detalle(self):
        return f"{self.marca} {self.modelo} ({self.color}, {self.año})"

class Mantenimiento:
    def __init__(self):
        self.registro_mantenimientos = []

    def agregar_mantenimiento(self, fecha, tipo):
        self.registro_mantenimientos.append((fecha, tipo))

    def mostrar_mantenimientos(self):
        return self.registro_mantenimientos

class Coche(Vehiculo, Mantenimiento):
    def __init__(self, marca, modelo, color, año, kilometraje, tipo_combustible, capacidad_pasajeros):
        Vehiculo.__init__(self, marca, modelo, color, año, kilometraje)
        Mantenimiento.__init__(self)
        self.tipo_combustible = tipo_combustible
        self.capacidad_pasajeros = capacidad_pasajeros

class Motocicleta(Vehiculo, Mantenimiento):
    def __init__(self, marca, modelo, color, año, kilometraje, cilindrada):
        Vehiculo.__init__(self, marca, modelo, color, año, kilometraje)
        Mantenimiento.__init__(self)
        self.cilindrada = cilindrada

class Camion(Vehiculo, Mantenimiento):
    def __init__(self, marca, modelo, color, año, kilometraje, capacidad_carga):
        Vehiculo.__init__(self, marca, modelo, color, año, kilometraje)
        Mantenimiento.__init__(self)
        self.capacidad_carga = capacidad_carga

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, año, tipo_bicicleta):
        Vehiculo.__init__(self, marca, modelo, color, año, 0) # Kilometraje no aplicable
        self.tipo_bicicleta = tipo_bicicleta

class PatinetaElectrica(Vehiculo):
    def __init__(self, marca, modelo, color, año, autonomia_bateria):
        Vehiculo.__init__(self, marca, modelo, color, año, 0) # Kilometraje no aplicable
        self.autonomia_bateria = autonomia_bateria

# Lista para almacenar objetos
vehiculos = []

coche1 = Coche("Toyota", "Corolla", "Rojo", 2020, 15000, "Gasolina", 5)
moto1 = Motocicleta("Yamaha", "YZF-R3", "Azul", 2019, 8000, 321)
camion1 = Camion("Volvo", "VNL 860", "Blanco", 2021, 5000, 40000)
bicicleta1 = Bicicleta("Trek", "Marlin", "Negro", 2021, "Montaña")
patineta1 = PatinetaElectrica("Xiaomi","Scooter 4 pro", "Negro", 2022, 55)

vehiculos.append(coche1)
vehiculos.append(moto1)
vehiculos.append(camion1)
vehiculos.append(bicicleta1)
vehiculos.append(patineta1)

with open("vehiculos.txt", "w") as file:
    for vehiculo in vehiculos:
        file.write(f"{vehiculo.marca}, {vehiculo.modelo}, {vehiculo.color}, {vehiculo.año}, {vehiculo.kilometraje}\n")

print(coche1.mostrar_detalle())
coche1.agregar_mantenimiento("2024-04-10", "Cambio de aceite")
print(coche1.mostrar_mantenimientos())

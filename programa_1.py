import os
from datetime import datetime

class PersonalUniversitario:
    def __init__(self, nombre, edad, codigo, fecha_ingreso):
        self.nombre = nombre
        self.edad = edad
        self.codigo = codigo
        self.fecha_ingreso = datetime.strptime(fecha_ingreso, '%d/%m/%Y')
    
    def calcular_antiguedad(self):
        antiguedad_total_dias = (datetime.now() - self.fecha_ingreso).days
        years = antiguedad_total_dias // 365
        dias = antiguedad_total_dias % 365
        return f'{years} años y {dias} días'

class Profesor(PersonalUniversitario):
    def __init__(self, nombre, edad, codigo, fecha_ingreso, tipo, horas_mensuales):
        super().__init__(nombre, edad, codigo, fecha_ingreso)
        self.tipo = tipo
        self.horas_mensuales = horas_mensuales
        self.materias = ["Cálculo", "Física", "Programación IV]"]
        self.salario = self.get_salario()
    
    def get_salario(self):
        salario = self.horas_mensuales * 15000
        return salario
    
    def mostrar_materias(self):
        for materia in self.materias:
            print(materia)

class Alumno(PersonalUniversitario):
    def __init__(self, nombre, edad, codigo, fecha_ingreso, carrera, semestre):
        super().__init__(nombre, edad, codigo, fecha_ingreso)
        self.carrera = carrera
        self.semestre = semestre
        
class ProfesorAyudante(Profesor, Alumno):
    def __init__(self, nombre, edad, codigo, fecha_ingreso, tipo, horas_mensuales, carrera, semestre):
        PersonalUniversitario.__init__(self, nombre, edad, codigo, fecha_ingreso)
        self.tipo = tipo
        self.horas_mensuales = horas_mensuales
        self.materias = ["Álgebra", "Estadística", "Programación I"]
        self.carrera = carrera
        self.semestre = semestre
        self.salario = Profesor.get_salario(self) - (self.horas_mensuales * 6000)


lista_personal = []
alumno = Alumno("Juan", 30, 123, "23/07/2022", "Ingenieria", 5)
profesor = Profesor("Pedro", 25, 124, "06/08/2020", "Tiempo completo", 160)
ayudante = ProfesorAyudante("Pedro", 25, 124, "01/01/2021", "Tiempo completo", 80, "Ingenieria", 5)

lista_personal.append(alumno)
lista_personal.append(profesor)
lista_personal.append(ayudante)

with open('personal.txt', 'w') as file:
    for personal in lista_personal:
        file.write(f'{personal.nombre}, {personal.edad}, {personal.codigo}, {personal.fecha_ingreso.strftime("%d/%m/%Y")}\n')
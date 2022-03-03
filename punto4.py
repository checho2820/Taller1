# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:16:39 2022

@author: sgomez34
"""

#Un alumno desea saber cuál será su calificación final en la materia de
#fundamentos de programación. Dicha calificación se compone de los
#siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
#calificación de un examen en clase y 20% de la calificación de un proyecto
#final.

notaTaller1 = int(input("Ingrese la nota del taller 1: "))
notaTaller2 = int(input("Ingrese la nota del taller 2: "))
notaTaller3 = int(input("Ingrese la nota del taller 3: "))
notaExamen = int(input("Ingrese el valor del examen en clase: "))
notaProyecto = int(input("Ingrese la nota del proyecto final: "))
promTalleres = (notaTaller1 + notaTaller2 + notaTaller3) / 3
notaFinal = (promTalleres * 0.5) + (notaExamen * 0.3) + (notaProyecto * 0.2)
print(f'La nota final del estudinate es: {notaFinal}')
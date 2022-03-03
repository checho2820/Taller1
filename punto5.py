# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:30:50 2022

@author: sgomez34
"""

#Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el
#porcentaje de alumnos de cada uno de los cursos.

estRedes = int(input("Ingrese la cantidad de estudiantes de la clase de redes: "))
estCont = int(input("Ingrese la cantidad de estudiantes de la clase de contabilidad: "))
estDise = int(input("Ingrese la cantidad de estudiantes de la clase de diseño: "))
totalEst = estRedes + estCont + estDise

porcRedes = (estRedes/totalEst)*100
porcCont = (estCont/totalEst)*100
porcDise = (estDise/totalEst)*100

print(f'El total de alumnos de redes es: {estRedes}')
print(f'El total de alumnos de contaduria es: {estCont}')
print(f'El total de alumnos de diseño es: {estDise}')
print(f'El total de alumnos en general es: {totalEst}')


print(f'El porcentaje de los estudiantes de redes es de {porcRedes}%')
print(f'El porcentaje de los estudiantes de contaduria es de {porcCont}%')
print(f'El porcentaje de los estudiantes de diseño es de {porcDise}%')

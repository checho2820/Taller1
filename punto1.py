# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Una Institución educativa ha recibido una donación especial que será
#repartida entre las carreras de Telecomunicaciones, Sistemas,
#Administración y Contabilidad de la siguiente forma:
#a. Telecomunicaciones 10% del valor dado a sistemas
#b. Sistemas: 25% del valor dado a Administración
#c. Administración: 35% del valor de la donación
#d. Contabilidad: lo que resta de la donación

donation = int(input('Enter the value of the donation: '))
adminVal = donation * 0.35
sistVal = adminVal * 0.25
telecVal = sistVal * 0.1
aux = telecVal + sistVal + adminVal
contVal = donation - aux
print(f'Value of the donation is: ${donation}')
print(f'Value to admin is: ${adminVal}')
print(f'Value to system is: ${sistVal}')
print(f'Value to telecomunication is: ${telecVal}')
print(f'Value to accounting is: ${contVal}')




 
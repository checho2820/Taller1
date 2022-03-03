# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:49:10 2022

@author: sgomez34
"""

#Haga un programa en Python que permita ingresar el dinero invertido por
#tres personas para formar una empresa. Cada una de ellas invierte una
#cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
#al total de la inversión.

firstPers = int(input("Ingrese la inversion de la primera persona: "))
secPers = int(input("Ingrese la inversion de la segunda persona: "))
ThirdPers = int(input("Ingrese la inversion de la tercera persona: "))

sumTotal = firstPers + secPers + ThirdPers
porcenFirtPers = (firstPers/sumTotal)*100
porcenSecPers = (secPers/sumTotal)*100
porcenThirdPers = (ThirdPers/sumTotal)*100
print(f'El total de la inversión es de {sumTotal}')
print(f'La primera persona invirtió {firstPers} que representa el {porcenFirtPers}% del total de la inversión')
print(f'La segunda persona invirtió {secPers} que representa el {porcenSecPers}% del total de la inversión')
print(f'La tercera persona invirtió {ThirdPers} que representa el {porcenThirdPers}% del total de la inversión')
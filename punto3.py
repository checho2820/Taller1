# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:06:11 2022

@author: sgomez34
"""

#Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
#ventas efectuadas en el mes. El vendedor desea saber cuanto dinero en
#total obtendrá por las ventas que realiza en el mes. Desarrolle un programa
#en Python que permita mostrar el valor ganado por comisión y el valor total
#a pagar al vendedor.


sueldoBase = int(input('Ingrese el valor del sueldo base del empleado: '))
ventasMes = int(input('Ingrese el valor de las ventas efectuadas en el mes: '))
comision = ventasMes * 0.15
valorTotal = sueldoBase + comision
print(f'El sueldo base del empleado es: ${sueldoBase}')
print(f'El valor ganado por comisión es de: ${comision}')
print(f'El valor total a pagar al empleado es: ${valorTotal}')

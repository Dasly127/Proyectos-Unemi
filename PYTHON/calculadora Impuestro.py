'''
Entrada de datos: 
El programa solicita al usuario que ingrese dos valores: 
el monto del pago sin impuesto (pago_sin_impuesto) y el monto del impuesto en porcentaje (monto_impuesto).
Definición de la función: Se define una función llamada calcular_total_pago que toma dos argumentos: 
pago_sin_impuesto y monto_impuesto. Esta función calcula el total del pago incluyendo el impuesto.
Cálculo del total con impuesto: Dentro de la función, 
se calcula el monto del impuesto multiplicando el pago_sin_impuesto por monto_impuesto/100 para obtener el porcentaje del impuesto. 
Luego, se suma este impuesto al pago_sin_impuesto para obtener el pago_total, que es el monto total a pagar incluyendo el impuesto.
Llamada a la función y salida: Se llama a la función calcular_total_pago con los valores ingresados por el usuario. 
El resultado devuelto por la función (el total con impuesto) se almacena en la variable total_con_impuesto. Finalmente, se imprime el resultado al usuario.
'''




pago_sin_impuesto = float(input("Ingrese el valor del pago sin impuesto:  "))

monto_impuesto = float(input("Ingrese el valor del del impuesto:  "))


def calcular_total_pago(pago_sin_impuesto, monto_impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (monto_impuesto/100)
    return pago_total

#Llamado a la función
total_con_impuesto = calcular_total_pago(pago_sin_impuesto, monto_impuesto)


print(f"Tu precio total incluyendo impuestos es: {total_con_impuesto}")
import math as m

import numpy as np
import matplotlib as plt
def rendimientos_acciones():
    precio_dolar_pesos_1 = 18.16
    precio_dolar_pesos_2 = 18.00

    precio_dolar_actual = float(input('Precio actual del dolar:\r\n'))

    inv_pesos_1 = 10000
    precio_ac_1 =185

    inv_pesos_2 = 3841.66
    precio_ac_2 = 165

    num_acc_compra_1 = (inv_pesos_1/precio_dolar_pesos_1)/precio_ac_1
    num_acc_compra_2 = (inv_pesos_2/precio_dolar_pesos_1)/precio_ac_2

    total_acc = num_acc_compra_1 + num_acc_compra_2

    print('========================================================')
    print(f'Usted compro {num_acc_compra_1} a un precio de {precio_ac_1} dolares')
    print(f'Usted compro {num_acc_compra_2} a un precio de {precio_ac_2} dolares')
    print(f'En total tiene {total_acc} invertidas en Tesla')
    print('========================================================')

    #Rendimiento en funcion del precio de venta:

    precio_venta = float(input('Ingrese el precio de venta de las acciones:\r\n'))

    rend_1 =(num_acc_compra_1*precio_venta) - (num_acc_compra_1*precio_ac_1)
    rend_MXN_1 = rend_1*precio_dolar_actual

    rend_2 =(num_acc_compra_2*precio_venta) - (num_acc_compra_2*precio_ac_2)
    rend_MXN_2 = rend_2*precio_dolar_actual

    print('===============================================================================================================================')
    print(f'Usted esta ganando ${rend_1} dolares por las acciones de ${precio_ac_1} dolares equivalente a $ {rend_MXN_1} pesos mexicanos ')
    print(f'Usted esta ganando ${rend_2} dolares por las acciones de ${precio_ac_2} dolares equivalente a $ {rend_MXN_2} pesos mexicanos ')
    print('===============================================================================================================================')

    rend_total = rend_1 + rend_2
    rend_total_MXN = rend_total*precio_dolar_actual


    print(f'Usted a generado en total ${rend_total} dolares quivalente a ${rend_total_MXN} pesos mexicanos')
    print('===============================================================================================================================')

rendimientos_acciones()

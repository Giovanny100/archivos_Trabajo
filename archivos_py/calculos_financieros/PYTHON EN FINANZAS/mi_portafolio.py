portafolio  = {
    'gbm fija' : [200,200],
    'acciones externas' : [100,205],
    'acciones mx' : [315,265,123],
    'cetes' : []
    }

'''
CONSULTA DE GANANCIAS DE UN PLAN DE INVERSION ESPECIFICO
'''

# #Agregar la funcionalidad de que puedan irse agregando automaticamente los datos a el diccionario

# #Preguntar de cual de las inversiones desea consultar su ganancia:

# plan_de_inversion = input('¿Que plan de inversion desea consultar?\r\n')

# #Suma de inversiones el plan que decea consultar (llamado directamente de la lista del diccionario):

# suma = sum(portafolio[plan_de_inversion])

# #Preguntar y pedir entrada del valor del plan que decea consultar:

# valor_actual = float(input(f'Cuanto vale su inversión en {plan_de_inversion} ahora mismo: \r\n'))

# #Devolver la ganancia del plan consultado hasta la fecha actual:

# print(f'Usted a generado hata ahora $ {valor_actual - suma} en {plan_de_inversion}')

'''
GANANCIA TOTAL DE LAS INVERSIONES:
'''

#Cuanto generé en el año:

print('PARA CONSULTAR SUS GANANCIAS TOTALES ACTUALMENTE POR FAVOR PROPORCIONE LOS SIGUIENTES DATOS:')

#Caclular la inversion total del usuario por me dio de la suma de la lisa del diccionario en cada plan de inversion:

inv_total = sum(portafolio['gbm fija'] + portafolio['acciones externas'] + portafolio['acciones mx']+ portafolio['cetes'])

#Pedir los precios actuales de cada plan de inversion:

valor_actual_gbm_fijo = float(input('valor de inversión en GBM fijo actual: \r\n'))

valor_actual_acciones_mx = float(input('valor de inversión en acciones MX actual: \r\n'))

valor_actual_acciones_externas = float(input('valor de inversión acciones en externas actual: \r\n'))

valor_actual_cetes = float(input('valor de inversión en cetes actual: \r\n'))

#Calculo del valor total de inversiones actualemnte:

valor_total_actual = valor_actual_gbm_fijo + valor_actual_acciones_mx + valor_actual_acciones_externas + valor_actual_cetes

#Calcular la plusvalia de las inversiones:

total_de_dinero_generado = valor_total_actual - inv_total

print(f'Su inversion total hasta ahora es: $ {inv_total}\r\n Actualmente tiene: {valor_total_actual} \n\r Usted ha generado: $ {total_de_dinero_generado} desde 2 de enero del 2023')

'''
CONSULTA DEL PLAN DE INVERSION CON MAYOR GANANCIA Y RENDIMIENTO
'''

ganancia_gbm_fija = valor_actual_gbm_fijo - sum(portafolio['gbm fija'])
ganancia_acciones_externas = valor_actual_acciones_externas - sum(portafolio['acciones externas'])
ganancia_acciones_mx = valor_actual_acciones_mx - sum(portafolio['acciones mx'])
ganancia_cetes = valor_actual_cetes - sum(portafolio['cetes'])

#Devolver una tabla con la ganancia de cada una de las inversiones :

print(f'USTED A ACUMULADO LAS SIGUIENTES CANTIDADES: \r\n GBM Tasa Fija: $ {ganancia_gbm_fija} \r\n Acciones externas: $ {ganancia_acciones_externas} \r\n Acciones MX: {ganancia_acciones_mx} \r\n CETES: $ {ganancia_cetes}'  )





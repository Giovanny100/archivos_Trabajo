
ganancias = int(input('Ingrese la cantidad de ganancias anuales:\r\n'))
trabajadores = int(input('Ingrese el numero de trabajadores:\r\n'))
salarios = int(input('Ingrese el salario mensual promedio de los trabajadores:\r\n'))
dias_sueldo = int(input('Ingrese los dias de sueldo por derecho:\r\n'))

aguinaldo = dias_sueldo*(salarios/30)
total_anual_aguinaldos = aguinaldo*trabajadores
salarios_total = salarios*trabajadores*12
reinversiones = 0.4*ganancias

tot_lib = ganancias - (total_anual_aguinaldos + salarios_total + reinversiones)

print('================================================================================================')


print(f'Se daran ${salarios} MXN mensuales ')
print(f'Se dara anualmente ${aguinaldo} MXN a cada empleado de aguinaldo')

print('================================================================================================')

print(f'Se reinvertira anualmente (deudas y mejoras) ${reinversiones} MXN ')
print(f'Se dara anualmente ${salarios_total} MXN de salarios')
print(f'Se dara anualmente ${total_anual_aguinaldos} MXN de aguinaldos')

print('================================================================================================')

print(f'La ganancia total libre es $ {tot_lib}')

print('================================================================================================')

print(f'Usted ganaria mensualemtne $ {tot_lib/12} MXN')

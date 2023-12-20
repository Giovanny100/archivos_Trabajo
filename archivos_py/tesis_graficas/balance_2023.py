
#? INGRESOS MENSUALES:

#? Empleo = $10000
#? Tocar = $1000
#? Venta = $200

#! GASTOS MENSUALES:


# ! Los gastos estan divididos en:
# ! Deuda coopel = $2500
# ! Deuda BBVA = $650
# ! Deuda traje = $610
# ! Terapias Mariana = $600
# ! Comida misty = $320
# ! Arena misty = $420
# ! Pasajes (mes) = $750
# ! Pago izzi = $300
# ! Despensa (mes) = $500
# ! Ahorro (mes) = $300
# ! Celular (mes) = $ 800

gastos_mes = 2500+(2*650)+610+600+320+300+750+300+500+300+800

print(f' Tus gastos son de: ${gastos_mes} al mes')

print(f' Tu restante mensual es: ${10000 - gastos_mes}')

#! Comprometerme a que cada cantidad que salga de la TDC BBVA sea remplzada con dinero de tocar
#! Por lo tanto tengo que conseguir minimo al mes $1000 tocando ($250 a la semana) para liberar por lo menos los gastos de la gata.
#! Esto sera posible si me voy por lo menos tres veces a tocar en la semana y saco aprox $100 pesos

#* SI SACO MAS DE LOS MIL HABRA QUE REPONERLOS CON MAS DIAS DE TOCAR
#* DEBO SALIR LUNES, MIERECOLES Y VIERNES O BIEN MARTES, VIERNES Y DOMINGOS

#* ASUMIENDO QUE TOCARA ENTRE SEMANA SEGUN LO ACORDADO ANTERIORMENTE + UNA VENTA DE $# 200 AL MES:


print(f' Tu restante mensual + 3 dias x semana de tocar es: ${10000 + 1000 +200 - gastos_mes}')
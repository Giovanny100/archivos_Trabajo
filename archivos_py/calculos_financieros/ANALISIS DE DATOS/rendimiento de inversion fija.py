
'''
inv_ini = Inversion incicial [=] $ Divisa
t_a = Tasa anual [=] %
plazo =Tiempo de interes de rendimientos [=] años
'''
def rendimiento_diario(io,t_a,plazo):
    rend = (io*(t_a/100))/(plazo)
    # print(f'Usted ganara $ {rend}  MXN diarios')
    return rend

bbva =rendimiento_diario(4280.71,8.75,365)

cetes = rendimiento_diario(5995.12,6.7,1)

bondia = rendimiento_diario(3.44,5.2,1)

rend_tot = cetes + bondia
print(rend_tot)

rend_bbva =bbva

print(rend_bbva)




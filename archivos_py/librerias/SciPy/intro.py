
#' SciPy (Pyton Cientifico)

#' Es una libreria de calculos cientrificos que usa Numpy
#' Ofrece funciones utiles para optimización, estadisticas y procesamiento de señales
#'La ventaja que ofrece ante Numpy son sus fucniones optimizadas para ciencia de datos

#' Una de las ventajas que ofrece es que proporciona constantes matematicas

from scipy import constants

#c Podemos ver todas las constantes de scipy:

# print(dir(constants))

# Consultar la constante pi:

# print(constants.pi)

#' PREFIJOS METRICOS

# print(constants.yotta)    #* 1e+24
# print(constants.zetta)    #* 1e+21
# print(constants.exa)      #* 1e+18
# print(constants.peta)     #* 1000000000000000
# print(constants.tera)     #* 1000000000000
# print(constants.giga)     #* 1000000000
# print(constants.mega)     #* 1000000
# print(constants.kilo)     #* 1000
# print(constants.hecto)    #* 100
# print(constants.deka)     #* 10
# print(constants.deci)     #* 0.1
# print(constants.centi)    #* 0.01
# print(constants.milli)    #* 0.001
# print(constants.micro)    #* 1e-06
# print(constants.nano)     #* 1e-09
# print(constants.pico)     #* 1e-12
# print(constants.femto)    #* 1e-15
# print(constants.atto)     #* 1e-18
# print(constants.zepto)    #* 1e-21

# #' PREFIJOS BINARIOS

# #' Devulve la unidad especifica en byts

# print(constants.kibi)    #*1024
# print(constants.mebi)    #*1048576
# print(constants.gibi)    #*1073741824
# print(constants.tebi)    #*1099511627776
# print(constants.pebi)    #*1125899906842624
# print(constants.exbi)    #*1152921504606846976
# print(constants.zebi)    #*1180591620717411303424
# print(constants.yobi)    #*1208925819614629174706176

# #' En general scipy cuenta con varias categorias de unidades

# #' Mass (devuelve la unidad especificada en kilogramos)

# print(constants.lb)          #*0.45359236999999997

# #' Angle (devuelve la unidad especificada en radianes)

# print(constants.degree)     #* 0.017453292519943295

# #' Time (devuelve la unidad especificada en segundos)

# print(constants.hour)        #* 3600

# #' Length (devuelve la unidad especificada en metros)

# print(constants.inch)              #* 0.0254
# print(constants.foot)              #* 0.30479999999999996

# #' Pressure (devuelve la unidad especificada en pascales)

# print(constants.atm)         #* 101325.0
# print(constants.bar)         #* 100000.0
# print(constants.torr)        #* 133.32236842105263
# print(constants.mmHg)        #* 133.32236842105263
# print(constants.psi)         #* 6894.757293168361

# #' Volume (devuelve la unidad especificada en metros cubicos)

# print(constants.litre)            #* 0.001
# print(constants.gallon)           #* 0.0037854117839999997
# print(constants.gallon_US)        #* 0.0037854117839999997

# #' Speed (devuelve la unidad especificada en metros por segundo)

# print(constants.kmh)            #* 0.2777777777777778

# #' Temperature (devuelve la unidad especificada en Kelvin)

# print(constants.zero_Celsius)      #* 273.15
# print(constants.degree_Fahrenheit) #* 0.5555555555555556

# #' Energy (devuelve la unidad especificada en Joules)

# print(constants.calorie)       #* 4.184
# print(constants.calorie_th)    #* 4.184
# print(constants.calorie_IT)    #* 4.1868
# print(constants.erg)           #* 1e-07
# print(constants.Btu)           #* 1055.05585262

# #' Power (devuelve la unidad especificada en Watts)

# print(constants.hp)         #* 745.6998715822701

# #' Force (devuelve la unidad especificada en newtons)

# print(constants.dyne)            #* 1e-05
# print(constants.lbf)             #* 4.4482216152605
# print(constants.pound_force)     #* 4.4482216152605
# print(constants.kgf)             #* 9.80665


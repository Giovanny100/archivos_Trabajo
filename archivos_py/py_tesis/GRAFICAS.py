#GRAFICO DE USOS DE AGUA EN MEXICO:

import matplotlib.pyplot as plt

# porcentajes = [76,14,5,5]
# usos = ["Agrícola:76%","Abastecimiento público:14%","Ind. autoabastecida: 5%","Termoelectricas: 5%"]
# colores = ["#EE3999","#10D394","#BBF919","#FFD97D","#FF9B85"]
# plt.pie(porcentajes, labels=usos, autopct="%0.1f %%", colors=colores)
# plt.axis("equal")
# plt.show()

#GRAFICO DE BARRAS (DISPONIBILIDAD DE AGUA POR HABITANTE)
from matplotlib import pyplot

año = ['', '1925', '1981', '2028']
valores = [0, 31000, 9800, 3650]
colores = ['#FFD1DC', '#FF69B4', '#FFAEB9', '#FFC0CB']

pyplot.title('DISPONIBILIDAD DE AGUA POR HABITANTE (m3/año)')
pyplot.bar(año, height=valores, color=colores, width=0.3)

# Ajustar límites del eje x para acortarlo
pyplot.xlim(0.5, len(año) - 0.5)

pyplot.show()


#GRAFICAS DE DISPONIBILIDAD DEL AGUA SEGUN SEMARNAT

import matplotlib.pyplot as plt

# dist_water = [97.5,2.5]
# tipo_w = ["Oceanos","Agua Dulce"]
# colores = ["#FF9B85","orangered"]
# plt.pie(dist_water, labels=tipo_w, autopct="%0.1f %%", colors=colores)
# plt.axis("equal")
# plt.show()

# dist_2 = [68.7,0.8,30,0.4]
# tipo_2 = ["Glaciares","Premafrost","Agua subterranea","Aguas superficiales"]
# colores_2 = ["Moccasin","Gold","PeachPuff","Yellow"]
# plt.pie(dist_2, labels=tipo_2, autopct="%0.1f %%", colors=colores_2)
# plt.axis("equal")
# plt.show()

# #USOS DEL AGUA DULCE
# dist_2 = [0.8,1.6,8.5,9.5,12.2,67.4]
# tipo_2 = ["Plantas y animales","Ríos","Otros humedales","Atmósfera","Humedad del suelo","Lagos de agua dulce"]
# colores_2 = ["palevioletred","hotpink","violet","plum","LightSalmon","lightpink"]
# plt.pie(dist_2, labels=tipo_2, autopct="%0.1f %%", colors=colores_2)
# plt.axis("equal")
# plt.show()

#GRAFICO PRODUCCION DE VINO

#GRAFICO DE BARRAS (DISPONIBILIDAD DE AGUA POR HABITANTE)
# from matplotlib import pyplot
# año = ['','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

# valores = ['','257.5','261.1','253.2','226.5','242.4','228.5','273.3','271.4','309.1','351.7','374','527']

# colores = ['white','pink','deeppink','thistle',"lightpink","hotpink","violet","plum","palevioletred","mediumvioletred","darkmagenta","magenta","purple"]

# pyplot.title('PRODUCCION DE TEQUILA EN MEXICO (MILLONES DE LITROS)')

# pyplot.bar(año,height = valores, color = colores, width = 0.3)

# pyplot.show()

#PORCENTAJE DE EMISION DE METANO DE EFLUETNES INDUSTRIALES:

#GRAFICO DE BARRAS (DISPONIBILIDAD DE AGUA POR HABITANTE)

# import matplotlib.pyplot as plt

# porcentajes = [68.17,4.15,1.01,0.11,4.13,4.86,1.85,0.05,2.98,10.76,0.81,0.57,0.1,0.09,0.07]
# usos = ["Papel","Frutas y Jugos","Refrescos","Aceite y Grasa",'Procesamiento de pescado','Azucar','Productos Lacteos','Vino','Cerveza','Carnes',
# 'Sustancias quimicas organicas','Textiles naturales','Refinacion de alcoholes','Jabon y detergentes','Otros']
# colores = ["#EE3999",'pink','deeppink','thistle',"lightpink","hotpink","violet","plum","palevioletred","mediumvioletred","darkmagenta","magenta","purple","#FF9B85",'lavenderblush']
# explode = [0.5, 0, 0.4, 0.4, 0.4, 0, 0, 0, 0.4, 0, 0, 0.3, 0.4, 0.5, 0.6]

# fig, ax = plt.subplots()
# ax.pie(porcentajes, labels = usos,
#           colors = colores,
#           autopct='%.0f%%',
#           explode = explode,
#           shadow = True,
#           startangle = 180)

# ax.set_title('PORCENTAJE DE EMISION DE METANO DE EFLUETNES INDUSTRIALES')
# plt.show()

#GRAFICA DE CO2 COMO CONSECUENCIA DEL METANO:

# from matplotlib import pyplot
# año = ['','Carnes', 'Cerveza', 'Vino', 'Productos Lacteos', 'Azucar', 'Procesamiento de pezcado', 'Aceite y Grasa', 'Refrescos', 'Frutas y Jugos', 'Papel',
# 'Otros', 'Jabon y Detergentes', 'Refinacion de alcoholes','Textiles','Sustancias químicas orgánicas']

# valores = ['','88.66','24.57','0.38','15.22','40.03','34.02','0.92','8.29','34.22','561.73','3.03','0.74','0.86','4.67','6.65']

# colores = ['white','pink','deeppink','thistle',"lightpink","hotpink","violet","plum","palevioletred","mediumvioletred","darkmagenta","magenta","purple",'deeppink','thistle',"lightpink"]

# pyplot.title('PRODUCCION DE TEQUILA EN MEXICO (MILLONES DE LITROS)')

# pyplot.bar(año,height = valores, color = colores, width = 0.1)

# pyplot.show()


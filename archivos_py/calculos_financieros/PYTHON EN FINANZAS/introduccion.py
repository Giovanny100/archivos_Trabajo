'''
Entre las aplicaciones de python se encuentra el area financiera.
Con pyton podemos hacer analisis financiero (calcular metricas, generar reportes, automatizar varias tareas)

CONCEPTOS PREVIOS DE FINANZAS:
TICKER: ES UN CODIGO QUE HACE REFERENCIA A LAS ACCIONES DE UNA COMPAÑIA COTIZADA EN EL MERCADO DE VALORES.

STOCK: PRODUCTOS ALMACENADOS A ESPERA DE SU VENTA O BIEN ACCIONES

IVA (IMPUESTO SOBRE EL VALOR AÑADIDO):AUMENTO DE UN PORCENTAJE SOBRE EL PRECIO DE UN PRODUCTO O SERVICIO DEBIDO A LOS IMPUESTOS DE PRODUCCION DEL MISMO.

-IVA GENERAL: ES AL QUE ESTAN SUJETAS TODAS LAS VENTAS Y ES DEL 21%

-IVA REDUCIDO: 10% QUE SE APLICA SOBRE LOS SIGUIENTES CASOS:
En las entregas de alimentos destinados al consumo humano o animal, sin incluir las bebidas alcohólicas. También a la venta de animales, vegetales y demás productos utilizados para la obtención de alimentos.
La venta de productos agrícolas, forestales o ganaderos (Semillas, fertilizantes, insecticidas, herbicidas, etc.)
El consumo de agua.
Los productos o instrumentos sanitarios, así como los complementos destinados a subsanar deficiencias físicas, como las gafas.
La venta de viviendas, incluidas las plazas de garaje y anexos.
Los transportes de viajeros y sus equipajes.
Los servicios de hostelería.
Los servicios efectuados en favor de titulares de explotaciones agrícolas, forestales o ganaderas.
Los servicios de limpieza de vías públicas.
Las ejecuciones de obras de renovación y reparación realizadas en viviendas.
Los arrendamientos con opción de compra viviendas, incluidas las plazas de garaje y anexos.
Las ejecuciones de obras, consecuencia de contratos directamente formalizados entre el promotor y el contratista, que tengan por objeto la construcción o rehabilitación de viviendas.
Las importaciones de objetos de arte, antigüedades y objetos de colección.

-IVA SUPERREDUCIDO: 4% QUE APLICA SOBRE:
Venta de alimentos no elaborados, como el pan, harina, huevos, leche, quesos, frutas, verduras, hortalizas, legumbres, tubérculos y cereales.
Venta de libros, periódicos y revistas que no contengan única o fundamentalmente publicidad.
Venta de medicamentos.
Venta de vehículos para minusválidos.
Venta de prótesis o implantes.
Entrega de viviendas de protección oficial realizadas por el promotor, incluidos los garajes y anexos. Así como a su arrendamiento con opción de compra.
Los servicios de teleasistencia, ayuda a domicilio, centro de día y de noche y atención residencial.

MARGEN DE BENEFICIO BRUTO: INDICADOR DE PERDIDAS O GANANCIAS DESCONTANDO IMPUESTOS.

MARGEN_BENEFICIO = BENEFICIO/INGRESO * 100 = PRECIO_VENTA - COSTO_PROD / COSTO_PROD * 100

¿Que significa ROE?

Rentabilidad de recusos propios por sus siglas en ingles 'Return on Equity' es un indicador que mide el beneficio que obtiene una empresa en relacion a los recursos
propios, sin contabilizar recursos de terceros (endeudamiento).

Calcular metricas financieras basicas
Hacer graficos basados en datos financieros
Recuperar y analizar precios de las acciones
Hacer analisis financieros de las acciones y portafolios, incluyendo recuperacion de acciones,correlaciones y analissi de riesgos.
Optimizar un portafolio utilizando el simulador Monte Carlo

Construiremos un programa para analizar el precio del bitcoin (es una divisa digital descentralizada), descentralizada quiere decir que no solo son controladas por
un banco o empresa.

IMPORTAR PAQUETES:

Algunos paquetes de python tienen funciones utilies en finanzas que entre otras cosas permiten calcular la taza interna de retorno, calculo de interes compuesto,etc.

Una de las librerias que podemos utilizar es math, la cuál se usa para calculos matematicos
Es necesario importarla.

Para llamar a una funcion necesitamos llamar el nombre de la paqueteria, punto y luego el nombre de la funcion
'''

import math as m

x = m.sqrt(2)
print(x)

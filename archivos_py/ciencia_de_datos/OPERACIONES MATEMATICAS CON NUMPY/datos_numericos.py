'''
Los conjuntos de datos provienen de una amplia gama de fuentes y formatos: pueden ser colecciones de medidas numéricas, corpus de texto, imágenes, clips de audio o
básicamente cualquier cosa. No importa el formato, el primer paso en la ciencia de datos es transformarlo en matrices de números.

Recopilamos 45 alturas de presidentes de EE. UU. en centímetros en orden cronológico y las almacenamos en una lista, un tipo de datos integrado en Python.
'''

heights = [189,170,189,163,183,171,185,168,173,183,173,173,175,178,183,193,178,173,174,183,183,180,168,180,170,178,182,180,183,178,182,180,183,178,182,188,175,179,
183,193,182,183,177,185,188,182,185,191]

'''
En este ejemplo, George Washington fue el primer presidente y su altura era de 189 cm.

Si quisiéramos saber cuántos presidentes miden más de 188 cm, podríamos iterar a través de la lista, comparar cada elemento con 188 y aumentar el conteo en 1 a medida
que se cumplan los criterios.
'''

#generamos un contador:
cnt = 0

#iteramos sobre la lista:
for height in heights:
    if height > 188:
        cnt += 1
print(cnt)

'''
Esto muestra que hay cinco presidentes que miden más de 188 cm.
No importa el formato de los datos, el primer paso en la ciencia de datos es transformarlos en matrices de números.
'''

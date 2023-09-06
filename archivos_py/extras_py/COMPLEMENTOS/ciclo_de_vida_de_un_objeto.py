'''
EL CICLO DE VIDA DE UN OBJETO ESTA CONFORMADO POR SU CREACION, MANIPULACION Y DESTRUCCION.

LA PRIMERA ETAPA ES EL CICLO DE VIDA DE UN OBJETO ES LA DEFICICION DE LA CLASE A LA CUAL PERTENECE.

LA SIGUIENTE ETAPA ES LA INSTANCIACION DE UN OBJETO CUANDO __init__ ES LLAMADO. LA MEMORIA ES ASIGNADA PARA LAMACENAR LA INSTANCIA. JUSTO ANTES DE QUE EST OOCURRA, EL METODO __new__ DE LA CLASE
ES LLAMADO. ESTE ES NORMALMENTE REDEFINIDO SOLO EN CASO DE CLASES ESPECIALES.

LUEGO DE QUE OCURRA LO ANTERIRORES QUE EL OBJETO ESTAR LISTO PARA SER UTILIZADO.

Cuando un objeto es destruido, la memoria asignada se libera y puede ser utilizada para otros propósitos.
La destrucción de un objeto ocurre cuando su contador de referencias llega a cero. La cuenta de referencias es el número de variables y otros elementos que se refieren al objeto.
Si nada se está refiriendo al objeto (tiene una cuenta de referencias de 0) nada puede interactuar con este, así que puede ser eliminado con seguridad.
En algunas situaciones, dos (o más) objetos pueden solo referirse entre ellos, y por lo tanto pueden ser eliminados también.
La sentencia del reduce la cuenta de referencias de un objeto por uno, y a menudo conlleva a su eliminación.
El método mágico de la sentencia del es __del__.
El proceso de eliminación de objetos cuando ya no son necesarios se denomina recolección de basura.
En resumen, el contador de referencias de un objeto se incrementa cuando se le es asignado un nuevo nombre o es colocado en un contenedor (una lista, tupla o diccionario). La cuenta de
referencias de un objeto se disminuye cuando es eliminado con del, su referencia es reasignada, o su referencia sale del alcance. Cuando la cuenta de referencias de un objeto llega a cero,
Python automáticamente lo elimina.
'''



#' TEXTO PRINCIPAL
#* EXPLICAICONES
#? CODIGO


#' FREECAD
#' Para trabajar con freecad se usa python desde la consola del mismo software:

#! No hace falta importar las libreruas:

import FreeCAD
from FreeCAD import Part

#' 1. Lo mas basico de python en freeCAD es crear un objeto:

#* 1. Se define la variable que guardara el objeto
#* 2. Se usa el modulo Part del cual a la vez usamos make y en seguida el nombre de lo que queremos agregar, es decir (Part.make"objeto")
#* 3. Pasar los parametros del objeto que iran en funcion del tipo de geometria: cubo (l,l,l) ; cilindro(radio,altura); cono(radio,radio,altura)

#? box = Part.makeBox(1, 1, 1)

#*  Agrega el objeto de tipo (Part::Feature) al documento activo:
#* Shape: Conecta el cubo (Box) con el objeto que creamos

#? FreeCAD.ActiveDocument.addObject("Part::Feature", "MyBox").Shape = box

#* Este ultimo metodo de FreeCAD es para recalcular y mostrar actualizaciones hechas:

#?FreeCAD.ActiveDocument.recompute()

#' 2. Modificar las propidades del objeto:

#* Nombre del objeto existente que quieres modificar:

#? nombre_objeto = "MyBox"

#* Accede al objeto existente en el documento activo:

#? existing_object = FreeCAD.ActiveDocument.getObject(nombre_objeto)

#* Verifica si el objeto existe:

#? if existing_object:
    #* Modifica las propiedades del objeto:

    #? existing_object.Shape = Part.makeBox(3, 4, 2)  # Cambia las dimensiones

    #* Cambia la posición del objeto:

    #?translation_vector = FreeCAD.Vector(2, 1, 3)
    #?existing_object.Shape.translate(translation_vector)

    #* Actualiza la vista 3D:

    #?FreeCAD.ActiveDocument.recompute()
#?else:
    #?print(f"No se encontró un objeto con el nombre '{nombre_objeto}' en el documento activo.")


#' CAMBIAR NOMBRE DEL ARCHIVO:

#* Nombre actual del objeto que quieres cambiar:

nombre_objeto = "NombreAntiguo"

#* Nuevo nombre que deseas asignar al objeto
nuevo_nombre = "NuevoNombre"

#* Accede al objeto existente en el documento activo
existing_object = FreeCAD.ActiveDocument.getObject(nombre_objeto)

#* Verifica si el objeto existe
if existing_object:
    #* Cambia la etiqueta del objeto
    existing_object.Label = nuevo_nombre

    #* Actualiza la vista 3D
    FreeCAD.ActiveDocument.recompute()
else:
    print(f"No se encontró un objeto con el nombre '{nombre_objeto}' en el documento activo.")
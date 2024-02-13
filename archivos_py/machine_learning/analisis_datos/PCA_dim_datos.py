
                           #' ANALISIS DE COMPONENTES PRINCIPALES (REDUCCIÓN DE DIMENCION DE DATOS)

#' Es una técnica que se utiliza cuando hay muchas variables y no se puede visualizar tratando de conservar la mayor cantidad de información posible
#' Se basa en la suposicion de que a mayor varianza mayor información se tiene
#' Busca una proyección de los datos que genere una mayor varianza (mayor disperción de los datos sobre la linea proyectada)
#' Para maximizar la varianza nos apoyamos de algebra lineal (Vectores Eyn)

#? Revisar Técnicas de estadarización, normalización y escalamiento de datos para Machine learning
#*sklearn para lo anterior (modulo StandardScaler)

#c Ejemplo: Se quiere reducir un sistema de dos dimenciónes a una sola dimención por PCA
#c x =  Variable 1
#c y = Variable 2

#c 1. Normalizar los datos Z = (Xi - Med) / Desv    StandardScaler
#c 2. Calcular la matriz de covarianza (¿Cómo vairan las dos variables entre si? ¿Creciente o decreciente y que tan rapido lo hacen?) Pandas
#c 3. Encontrar los eigenvectores y eigenvalores (ortogonales que reprecentan los ejes del plano sobre los que vamos a proyectar los datos) Numpy
#c 4. Proyección de los datos


#' PRINCIPALES
#c DESCRIPCION
#* CONCEPTOS
#? PASOS A SEGUIR
#! EXTRAS


#' PRIMER HACKING ETICO CON PYTHON

#c Accederemos a la maquina victima desde la atacante solo con que la victima ejecute el 'archivo.py' que se debera encontrar en el escritorio para exponer sus datos
#c Para ejecutar el archivo desde el cmd debes abrir el escritorio desde cmd y escribir: python nombredelarchivo.py y enter
#c Lo anterior hara que se expongan los datos de donde se encuentra el archivo en el puerto especificado en el codigo

#* Servidor: Es un ordenador o particion del mismo el cual es muy potente y se encarga de almacenar y distribuir archivos para dar acceso a otros usuarios
#* Tambien puede ser un programa que ofrece una serie de servicios o entrega informacion tal como las computadoras

#c Tipos de servidores:

#* FTP: Sirven para mover archivos entre uno o mas ordenadores (es ofrecido por la capa de Aplicación del modelo TCP/IP y utiliza normalmente el puerto 20 y el 21)
#* FTPS/SSH: (File Transfer Protocol o Protocolo de Transferencia de Archivos mediante SSH) es un protocolo basado en SSH para la Transferencia Segura de Archivos.
#* SFTP utiliza la capa de transporte SSH para mover de forma segura grandes cantidades de información a través de una conexión a Internet (Puerto 22 acceder a servidores).
#* IRC: (Internet Reley Chat) Consiste en varias redes separadas que permite que los usuarios conecten por via red IRC
#* Bases de datos: Elite de los servidores (manejar grandes cantidades de datos)
#* Web: Almacenan los archivos html de una pagina web y los proporcionan a los usuarios por internet

#* Puerto: Es un servicio que corre por un ordenador (son identidficados con numeros por los ordenadores para saber a donde dirigir la informacion)
#* Para enviar y recibir archivos


import os

lista = os.system("python -m http.server 80")


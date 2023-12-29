from cryptography.fernet import Fernet
import os

from sklearn.model_selection import KFold

def generar_clave():
    return Fernet.generate_key()

def guardar_clave(clave, archivo):
    with open(archivo, 'wb') as archivo_clave:
        archivo_clave.write(clave)

def cargar_clave(archivo):
    return open(archivo, 'rb').read()

def encriptar_archivo(clave, archivo_original, archivo_encriptado):
    fernet = Fernet(clave)
    with open(archivo_original, 'rb') as f:
        datos = f.read()
        datos_encriptados = fernet.encrypt(datos)
    with open(archivo_encriptado, 'wb') as f_encriptado:
        f_encriptado.write(datos_encriptados)

def desencriptar_archivo(clave, archivo_encriptado, archivo_original):
    fernet = Fernet(clave)
    with open(archivo_encriptado, 'rb') as f:
        datos_encriptados = f.read()
        datos = fernet.decrypt(datos_encriptados)
    with open(archivo_original, 'wb') as f_original:
        f_original.write(datos)

# Cambia la ruta de la carpeta según tu escritorio
carpeta_encriptar = os.path.join(os.path.expanduser("~"), "Desktop", "holis")

# Verifica si la carpeta existe, si no, créala
if not os.path.exists(carpeta_encriptar):
    os.makedirs(carpeta_encriptar)

# Genera y guarda la clave
clave = generar_clave()
clave_archivo = os.path.join(carpeta_encriptar, 'clave.key')
guardar_clave(clave, clave_archivo)

# Encriptar archivos en la carpeta
for archivo_nombre in os.listdir(carpeta_encriptar):
    archivo_path = os.path.join(carpeta_encriptar, archivo_nombre)
    if os.path.isfile(archivo_path):
        encriptar_archivo(clave, archivo_path, archivo_path + '.encrypted')

# Desencriptar archivos en la carpeta (si es necesario)
for archivo_nombre in os.listdir(carpeta_encriptar):
    archivo_path = os.path.join(carpeta_encriptar, archivo_nombre)
    if os.path.isfile(archivo_path) and archivo_path.endswith('.encrypted'):
        desencriptar_archivo(clave, archivo_path, archivo_path[:-9])
import paramiko
import base64
import os
from stat import S_ISDIR

# 1. Configurar cliente SSH y registrar la clave de host conocida
client = paramiko.SSHClient()
key_b64 = b'AAAAC3NzaC1lZDI1NTE5AAAAIHS8HtKwh6UVIl6DnP5tfkmQfyQY4DaYFwyUx5z7K5Hb'
key = paramiko.Ed25519Key(data=base64.b64decode(key_b64))
client.get_host_keys().add('localhost', 'ssh-ed25519', key)

# Conectar al servidor SSH (cambia 'tu_contraseña_real' por tu contraseña de Linux)
client.connect('localhost', username='uo295465', password='Ser250404')
print("¡Conectado por SSH con éxito!\n")

# 2. Abrir el canal SFTP
sftp = client.open_sftp()

# Directorio remoto de origen y carpeta local de destino
carpeta_remota = '.'  # Directorio home del usuario por defecto
carpeta_local = '.'   # Carpeta local actual donde se guardarán las descargas

print(f"Analizando el contenido de la carpeta remota para descargar ficheros...")
elementos = sftp.listdir(carpeta_remota)

for nombre in elementos:
    # Ruta completa remota del elemento
    ruta_remota = f"{carpeta_remota}/{nombre}" if carpeta_remota != '.' else nombre
    ruta_local = os.path.join(carpeta_local, nombre)

    try:
        # Obtener los metadatos del fichero o directorio remoto
        atributos = sftp.stat(ruta_remota)

        # Comprobar si es un directorio usando S_ISDIR
        if S_ISDIR(atributos.st_mode):
            print(f"  [Omitido - Es un directorio]: {nombre}")
        else:
            print(f"  [Descargando fichero]: {nombre} ---> {ruta_local}")
            sftp.get(ruta_remota, ruta_local)
            
    except Exception as e:
        print(f"  [Error al procesar '{nombre}']: {e}")

# 3. Cerrar canal SFTP y conexión SSH
sftp.close()
client.close()
print("\n¡Proceso de descarga finalizado y conexiones cerradas correctamente!")

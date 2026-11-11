import paramiko
import base64

# 1. Configurar cliente SSH y añadir la clave de host conocida (Ejercicio 10)
client = paramiko.SSHClient()
key_b64 = b'AAAAC3NzaC1lZDI1NTE5AAAAIHS8HtKwh6UVIl6DnP5tfkmQfyQY4DaYFwyUx5z7K5Hb'
key = paramiko.Ed25519Key(data=base64.b64decode(key_b64))
client.get_host_keys().add('localhost', 'ssh-ed25519', key)

# 2. Conectar al servidor SSH (cambia 'tu_contraseña_real' por la tuya)
client.connect('localhost', username='uo295465', password='Ser250404')
print("¡Conectado por SSH con éxito!\n")

# 3. Abrir el canal SFTP sobre el transporte existente
sftp = client.open_sftp()

# 4. Obtener y mostrar el listado del directorio personal (home) por defecto
print(f"Listado de la carpeta del usuario ({sftp.getcwd() or '~'}):")
listado = sftp.listdir()

for nombre in listado:
    print(f" - {nombre}")

# 5. Cerrar sesión SFTP y conexión SSH
sftp.close()
client.close()
print("\nConexión SFTP y SSH cerradas correctamente.")

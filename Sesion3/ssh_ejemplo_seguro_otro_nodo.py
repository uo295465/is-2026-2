import paramiko
import time
import base64

# 1. Configurar los datos de la máquina remota del compañero
HOST_COMPAÑERO = '192.168.0.X'  # Sustituir por la IP de tu compañero
USUARIO_COMPAÑERO = 'uoXXXXXX'  # Sustituir por el usuario de tu compañero
CLAVE_COMPAÑERO = 'contraseña'   # Sustituir por la contraseña de tu compañero

# 2. Clave pública ED25519 del servidor de tu compañero (cadena base64 limpia)
b64_str_compañero = b'AAAAC3NzaC1lZDI1NTE5AAAAI...'  # Pegar la clave de tu compañero

key_bytes = base64.b64decode(b64_str_compañero)
key = paramiko.Ed25519Key(data=key_bytes)

# 3. Registrar la clave asociándola a la IP de tu compañero
client = paramiko.SSHClient()
client.get_host_keys().add(HOST_COMPAÑERO, 'ssh-ed25519', key)

# 4. Conectar a la máquina del compañero (aplica RejectPolicy por defecto)
client.connect(HOST_COMPAÑERO, username=USUARIO_COMPAÑERO, password=CLAVE_COMPAÑERO)
print(f"Conectado con éxito a {HOST_COMPAÑERO}!!")

# 5. Listar los archivos del directorio home de tu compañero
stdin, stdout, stderr = client.exec_command('ls -l')

for line in stdout:
    print(line.rstrip())

time.sleep(1)
client.close()
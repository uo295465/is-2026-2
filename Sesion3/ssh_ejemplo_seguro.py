import paramiko
import time
import base64

# 1. Clave pública del host en formato base64 binario de OpenSSH
b64_str = b'AAAAC3NzaC1lZDI1NTE5AAAAIHS8HtKwh6UVIl6DnP5tfkmQfyQY4DaYFwyUx5z7K5Hb'

key_bytes = base64.b64decode(b64_str)
key = paramiko.Ed25519Key(data=key_bytes)

# 2. Instanciar cliente SSH y registrar la clave confiable
client = paramiko.SSHClient()
client.get_host_keys().add('localhost', 'ssh-ed25519', key)

# 3. Conectar (recuerda poner tu contraseña real de Ubuntu)
client.connect('localhost', username='uo295465', password='Ser250404')
print("Conectado!!")

# 4. Ejecutar comando y mostrar salida
stdin, stdout, stderr = client.exec_command('ls')

for line in stdout:
    print(line.rstrip())

time.sleep(1)
client.close()
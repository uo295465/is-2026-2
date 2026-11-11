import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

# Esperar la solicitud de login y enviar el usuario
tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")

# Esperar la solicitud de contraseña y enviarla
if password:
    tn.read_until(b"Password")
    tn.write(password.encode('ascii') + b"\n")

# Enviar comandos al shell remoto
tn.write(b"ls /home\n")
tn.write(b"exit\n")

# read_all() lee hasta que el servidor cierra la conexión (por el comando exit)
# Decodificamos con 'utf-8' para soportar acentos y caracteres especiales
print(tn.read_all().decode('utf-8'))

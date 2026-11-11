import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Se lee y descarta todo el banner hasta recibir el prompt ($)
tn.read_until(b"$")

tn.write(b"ls /home\n")
tn.write(b"exit\n")

print("--- Salida limpia ---")
print(tn.read_all().decode('utf-8'))

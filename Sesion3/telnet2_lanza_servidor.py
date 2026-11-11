import telnetlib
import time

HOST = "localhost"
USER = "uo295465"
PASSWORD = "Ser250404"  

tn = telnetlib.Telnet(HOST)

# 1. Autenticación
tn.read_until(b"login: ")
tn.write(USER.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(PASSWORD.encode('ascii') + b"\n")

# 2. Esperar al prompt inicial ($)
tn.read_until(b"$")

# 3. Comprobar si el proceso existe usando pgrep -f
tn.write(b"pgrep -f udp_servidor3_con_ok.py\n")
salida_pgrep = tn.read_until(b"$").decode('utf-8')

# 4. Si pgrep devuelve algún número de PID, el proceso ya está corriendo
# (Filtramos las líneas vacías o del eco del comando)
lineas = [l.strip() for l in salida_pgrep.splitlines() if l.strip().isdigit()]

if len(lineas) > 0:
    print("El servidor ya está en ejecución (PID:", lineas[0] + ")")
    tn.write(b"exit\n")
else:
    print("El servidor NO está en ejecución. Lanzándolo con nohup...")
    tn.write(b"nohup python3 ~/udp_servidor3_con_ok.py &\n")
    time.sleep(1)
    tn.write(b"exit\n")

# 5. Salida de depuración
print("--- Respuesta final ---")
print(tn.read_all().decode('utf-8'))
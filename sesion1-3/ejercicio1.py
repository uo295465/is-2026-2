#sesion1-3
#ejercicio1
import sys
import socket
#leo la cantidad de argumentos 
if len(sys.argv) < 2:
	puerto = 9999
else:
	puerto= int(sys.argv[1], 10)#convierto argumernto en base 10
print("el puerto establecido es", puerto)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#creo socke udp
socket.bind(("",puerto))# lo asocio a todas las interfaces
while True:
	datagrama ,origen = socket.recvfrom(1024)
	print("Origen: ", origen)
	print("Informacion: ", datagrama.decode("utf-8"))
	socket.sendto(datagrama, origen)
	
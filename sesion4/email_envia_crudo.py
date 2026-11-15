
import socket
import sys


def RecvReply(sock, code):
    respuesta = sock.recv(1024)
    print(respuesta.decode(errors="replace"))

    if respuesta[:3] != code:
        print("ERROR: respuesta inesperada del servidor SMTP")
        sys.exit()


# Variables del programa
server = "relay.uniovi.es"
port = 25

fromaddr = "uo295465@uniovi.es"
toaddr = "uo295465@uniovi.es"

subject = "Prueba de correo SMTP"
data = "Este es un mensaje de prueba enviado desde Python usando sockets."

# Crear conexión TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

# 1. Recibir saludo inicial del servidor
RecvReply(s, b"220")

# 2. Identificarnos ante el servidor
s.sendall(("EHLO " + socket.gethostname() + "\r\n").encode())
RecvReply(s, b"250")

# 3. Indicar el remitente
s.sendall(("MAIL FROM:<" + fromaddr + ">\r\n").encode())
RecvReply(s, b"250")

# 4. Indicar el destinatario
s.sendall(("RCPT TO:<" + toaddr + ">\r\n").encode())
RecvReply(s, b"250")

# 5. Indicar que vamos a enviar el contenido
s.sendall(b"DATA\r\n")
RecvReply(s, b"354")

# 6. Construir el mensaje
message = (
    f"To: {toaddr}\r\n"
    f"From: {fromaddr}\r\n"
    f"Subject: {subject}\r\n"
    f"\r\n"
    f"{data}\r\n"
    f".\r\n"
)

# Enviar el mensaje
s.sendall(message.encode())
RecvReply(s, b"250")

# 7. Cerrar la conexión SMTP
s.sendall(b"QUIT\r\n")
RecvReply(s, b"221")

s.close()

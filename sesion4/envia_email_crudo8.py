
import socket
import sys
import email.message
import email.policy
import email.utils


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

subject = "Prueba de correo con EmailMessage"
data = "Hola, esta es una prueba utilizando la biblioteca email de Python."


# Crear conexión TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

# Recibir saludo inicial
RecvReply(s, b"220")

# Identificación del cliente
s.sendall(("EHLO " + socket.gethostname() + "\r\n").encode())
RecvReply(s, b"250")

# Indicar remitente
s.sendall(("MAIL FROM:<" + fromaddr + ">\r\n").encode())
RecvReply(s, b"250")

# Indicar destinatario
s.sendall(("RCPT TO:<" + toaddr + ">\r\n").encode())
RecvReply(s, b"250")

# Comenzar el envío del mensaje
s.sendall(b"DATA\r\n")
RecvReply(s, b"354")


# Construir el mensaje utilizando EmailMessage
mensaje = email.message.EmailMessage()

mensaje['To'] = toaddr
mensaje['From'] = fromaddr
mensaje['Subject'] = subject
mensaje['Date'] = email.utils.formatdate(localtime=True)
mensaje['Message-ID'] = email.utils.make_msgid()

mensaje.set_content(data)

# Convertir el mensaje a bytes con finales de línea SMTP (CRLF)
binario = mensaje.as_bytes(policy=email.policy.SMTP)

# Añadir el punto final que indica el final del mensaje SMTP
binario += b".\r\n"

# Enviar el mensaje
s.sendall(binario)
RecvReply(s, b"250")

# Terminar conexión
s.sendall(b"QUIT\r\n")
RecvReply(s, b"221")

s.close()

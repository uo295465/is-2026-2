import socket

# Función sugerida en la guía usando un bucle for y hex()
def mostrar_hex(respuesta):
    for byte in respuesta:
        print(hex(byte), end=" ")
    print()  # Salto de línea final

# Conexión en crudo por sockets al puerto Telnet (23)
s = socket.socket()
s.connect(("localhost", 23))
respuesta = s.recv(1024)

print("Respuesta directa de Python (bytes):")
print(respuesta)

print("\nRespuesta procesada byte a byte con hex():")
mostrar_hex(respuesta)

s.close()
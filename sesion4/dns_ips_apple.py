
import dns.resolver

respuesta = dns.resolver.resolve('apple.com', 'A')

for registro in respuesta:
    print(registro.address)

import socket
import sys
from parser import *

if len(sys.argv) != 6:
    print(
        "Uso: enviar.py IP_router_final puerto_router_final mensaje IP_envio puerto_envio"
    )
    sys.exit()

ip_final, puerto_final, mensaje, ip_envio, puerto_envio = sys.argv[1:]

paquete_plain = {
    "IP": ip_final,
    "Puerto": int(puerto_final),
    "Mensaje": mensaje.encode(),
}

paquete_bytes = create_packet(paquete_plain)

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sent = sckt.sendto(paquete_bytes, (ip_envio, int(puerto_envio)))
if sent > 0:
    print("envié algo")
else:
    print("no envié un carajo")

import socket
import sys

BUFFER_SIZE = 1024
sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def parse_packet(IP_packet):
    ip_codificada = IP_packet[:4]
    ip_decodificada = ""

    for i in range(4):
        octeto = ip_codificada[i]
        ip_decodificada += str(octeto)
        if i < 3:
            ip_decodificada += "."

    paquete = {"IP": ip_decodificada,
               "Puerto": int.from_bytes(IP_packet[4:6], "big"),
               "Mensaje": IP_packet[6:]}

    return paquete

def create_packet(parsed_IP_packet):
    l_ip = parsed_IP_packet["IP"].split(".")
    ip = b''
    for i in l_ip:
        ip += int.to_bytes(int(i), 1)
    port = int.to_bytes(parsed_IP_packet["Puerto"], 2)
    return ip + port + parsed_IP_packet["Mensaje"]

def tabulador(archivo):
    tabla = []
    with open(archivo, encoding="utf-8") as a:
        for linea in a:
            tabla.append(linea.split())
    return tabla

if (len(sys.argv) != 4):
    print("Se esperan 3 argumentos: IP, puerto y tabla de rutas")
    sys.exit()
else:
    ip = str(sys.argv[1])
    puerto = int(sys.argv[2])
    tabla = tabulador(sys.argv[3])

print("ip: ", ip)
print("puerto: ", puerto)
print("tabla: ", tabla)

sckt.bind((ip, puerto))

while True:
    message, direccion = sckt.recvfrom(BUFFER_SIZE)

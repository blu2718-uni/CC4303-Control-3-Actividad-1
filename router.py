import socket
import sys

from parser import *

BUFFER_SIZE = 1024
sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def en_red(ip, red):
    red_ip, prefijo = red.split("/")
    offset = int(prefijo) // 8
    return ip.split(".")[:offset] == red_ip.split(".")[:offset]

def check_routes(routes_file_name, destination_address):
    estructurado = tabulador(routes_file_name)
    for linea in estructurado:
        if (linea["Puerto Inicial"] <= destination_address[1]
        and linea["Puerto Final"] >= destination_address[1]
        and en_red(destination_address[0], linea["Red"])):
            return (linea["IP Salto"], linea["Puerto Salto"])
    return None

def tabulador(archivo):
    tabla = []

    with open(archivo, encoding="utf-8") as a:
        for linea in a:
            elementos = linea.split()
            tabla.append({"Red": elementos[0],
                          "Puerto Inicial": int(elementos[1]),
                          "Puerto Final": int(elementos[2]),
                          "IP Salto": elementos[3],
                          "Puerto Salto": int(elementos[4])})

    return tabla

if (len(sys.argv) != 4):
    print("Uso: IP, puerto y tabla de rutas")
    sys.exit()
else:
    ip = str(sys.argv[1])
    puerto = int(sys.argv[2])
    dir = (ip, puerto)
    tabla = tabulador(sys.argv[3])

print("ip: ", ip)
print("puerto: ", puerto)
print("tabla: ", tabla)

sckt.bind(dir)

while True:
    message, direccion = sckt.recvfrom(BUFFER_SIZE)
    message_parseado = parse_packet(message)
    if (message_parseado["IP"] == ip and message_parseado["Puerto"] == puerto):
        print(f"Se recibió un mensaje de: {direccion}")
        print(message_parseado["Mensaje"].decode())
    else:
        print(f"Se recibió un mensaje de: {direccion}")
        print(f"Fué reenviado a {direccion_salida}:{puerto_salida}")

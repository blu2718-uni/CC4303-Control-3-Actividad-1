import socket
import sys

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
    puerto = str(sys.argv[2])
    tabla = tabulador(sys.argv[3])

print("ip: ", ip)
print("puerto: ", puerto)
print("tabla: ", tabla)


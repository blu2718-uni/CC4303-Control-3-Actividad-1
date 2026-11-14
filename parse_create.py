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
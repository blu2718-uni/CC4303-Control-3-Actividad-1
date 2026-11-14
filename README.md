# Actividad 1 - Control 3 - Redes

La principal diferencia es que identificaremos distintas rutas a través de puertos distintos, no direcciones distintas. Otras diferencias incluyen la prescencia de flags e interfaces (ya que en a guia _Simulando un mini-internet_ no existen esos campos).

El punto 5 de esta actividad lo interpretamos de esta forma: La tupla (IP_router_final, puerto_router_final) lo interpretamos como el lugar a donde queremos enviar el paquete con el mensaje y el header. Mientras que la tupla (IP_envio, puerto_envio) es donde queremos que salga el paquete.

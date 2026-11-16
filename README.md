# Actividad 1 - Control 3 - Redes

> En esta actividad se usó Claude Opus 5.5 para consultas sobre firmas de funciones, funcionamiento de ciertas funciones en python y gestión del repositorio.

La principal diferencia es que identificaremos distintas rutas a través de puertos distintos, no direcciones distintas. Otras diferencias incluyen la presencia de flags e interfaces (ya que en la guía _Simulando un mini-internet_ no existen esos campos).

El punto 5 de esta actividad lo interpretamos de esta forma: La tupla (IP_router_final, puerto_router_final) lo interpretamos como el lugar a donde queremos enviar el paquete con el mensaje y el header. Mientras que la tupla (IP_envio, puerto_envio) es donde queremos que salga el paquete.

Se asume que los prefijos de red son múltiplos de 8 siempre.

A la hora de agregar un router default, el salto a ese router debe ubicarse al final de cada tabla de ruta que no sea la default. Por otro lado, la tabla de rutas del router default ha de apuntar directamente a cada uno de los otros routers.

La tabla de rutas del router default (`rutas/v5/rutas_Rd_v5.txt`) es:

```
127.0.0.1/24 8880 8880 127.0.0.1 8880
127.0.0.1/24 8881 8881 127.0.0.1 8881
127.0.0.1/24 8882 8882 127.0.0.1 8882
127.0.0.1/24 8883 8883 127.0.0.1 8883
127.0.0.1/24 8884 8884 127.0.0.1 8884
127.0.0.1/24 8885 8885 127.0.0.1 8885
127.0.0.1/24 8886 8886 127.0.0.1 8886
```

Haciendo el test de Mini-Internet sin TTL, tenemos los siguientes resultados:

1. Al enviar desde R1 a R3 con la versión 2 de las tablas, los router R1 y R2 loopean a medida que el mensaje va rebotando desde ambos. Esto pasa por el error de configuración descrito en el enunciado.
2. Para cada mensaje enviado a los routers según la versión 5 de las tablas de ruta, la cantidad de saltos es distinta. Enviando 10 paquetes de R1 a R5 intercalados con 10 de R5 a R1, se vieron desde 3 a 11 saltos (promedio de 7,6 saltos de R1 a R5 y de 5,1 de R5 a R1). El mínimo de 3 saltos dado por la topología de la red solo se alcanzó 2 veces de 20. Esto puede explicarse con la combinación del Round Robin con la configuración inicial de las tablas de ruta, donde el Round Robin va cambiando continuamente la configuración de los saltos a realizar a lo largo del viaje de un paquete.
3. Se tuvieron que crear varias tablas de ruta. Siendo las más "recientes" aquellas con el sufijo v5. Estas incluyen tanto el router 0 (R0) como el router por defecto (Rd). Con esta mayor cantidad de routers, la cantidad de saltos aumenta, pero su comportamiento parece el mismo que con las de la versión 3.

   Las tablas v4 son idénticas a las v5, pero sin la última línea (el salto al router default), y en v4 no existe Rd. La tabla de Rd está más arriba; el resto de las tablas v5 son:

   `rutas/v5/rutas_R0_v5.txt`
   ```
   127.0.0.1/24 8881 8881 127.0.0.1 8881
   127.0.0.1/24 8882 8886 127.0.0.1 8882
   127.0.0.1/24 0 65535 127.0.0.1 7000
   ```

   `rutas/v5/rutas_R1_v5.txt`
   ```
   127.0.0.1/24 8880 8880 127.0.0.1 8880
   127.0.0.1/24 8882 8886 127.0.0.1 8882
   127.0.0.1/24 8882 8886 127.0.0.1 8880
   127.0.0.1/24 0 65535 127.0.0.1 7000
   ```

   `rutas/v5/rutas_R2_v5.txt`
   ```
   127.0.0.1/24 8880 8881 127.0.0.1 8881
   127.0.0.1/24 8880 8881 127.0.0.1 8880
   127.0.0.1/24 8883 8886 127.0.0.1 8883
   127.0.0.1/24 8883 8886 127.0.0.1 8884
   127.0.0.1/24 8883 8886 127.0.0.1 8886
   127.0.0.1/24 0 65535 127.0.0.1 7000
   ```

   `rutas/v5/rutas_R3_v5.txt`
   ```
   127.0.0.1/24 8880 8882 127.0.0.1 8882
   127.0.0.1/24 8880 8882 127.0.0.1 8885
   127.0.0.1/24 8880 8882 127.0.0.1 8886
   127.0.0.1/24 8884 8886 127.0.0.1 8882
   127.0.0.1/24 8884 8886 127.0.0.1 8885
   127.0.0.1/24 8884 8886 127.0.0.1 8886
   127.0.0.1/24 0 65535 127.0.0.1 7000
   ```

   `rutas/v5/rutas_R4_v5.txt`
   ```
   127.0.0.1/24 8880 8883 127.0.0.1 8882
   127.0.0.1/24 8880 8883 127.0.0.1 8885
   127.0.0.1/24 8885 8886 127.0.0.1 8882
   127.0.0.1/24 8885 8886 127.0.0.1 8885
   127.0.0.1/24 0 65535 127.0.0.1 7000
   ```

   `rutas/v5/rutas_R5_v5.txt`
   ```
   127.0.0.1/24 8880 8884 127.0.0.1 8884
   127.0.0.1/24 8880 8884 127.0.0.1 8883
   127.0.0.1/24 8886 8886 127.0.0.1 8883
   127.0.0.1/24 0 65535 127.0.0.1 7000
   ```

   `rutas/v5/rutas_R6_v5.txt`
   ```
   127.0.0.1/24 8880 8882 127.0.0.1 8882
   127.0.0.1/24 8883 8885 127.0.0.1 8883
   127.0.0.1/24 0 65535 127.0.0.1 7000
   ```

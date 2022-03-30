#!/bin/bash
echo 
# tcpdump --list-interfaces  ( lista interfaces )
# tcpdump -w captura.pcap  ( guarda la captura en fichero captura.pcap )
# tcpdump host IP  ( captura todo lo entra y sale a una IP )
# tcpdump -s0 port 383  ( filta por puerto )
# tcpdump -s0 not port 22 and port 636 ( filtra por puerto y evita captura de otro )
# tcpdump -i eth0 udp
# tcpdump -i eth0 tcp
# tcpdump -i eth0 icmp
# tcpdump -i eth0 tcp port 80
# tcpdump -i eth0 udp port 53 -vv
# tcpdump -i eth0 -A ( Muestra los datos en Ascii )
# tcpdump -i eth0 -XX ( Muestra los datos en formato Hexadecimal y ascii )
# tcpdump -i eth0 -s0 -vvv not port 22 and port 636 -w /tmp/captura.pcap |stdbuf -oL tcpick -C -v -a -h -yP -r 
# tcpdump port http or port ftp or port smtp or port imap or port pop3 or port telnet -l -A | egrep -i -B5 'pass=|pwd=|log=|login=|user=|username=|pw=|passw=|passwd=|password=|pass:|user:|username:|password:|login:|pass |user '
tcpdump -i eth0 -s0 -vvv not port 22

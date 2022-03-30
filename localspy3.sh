#!/bin/bash
echo 
# tcpdump --list-interfaces  ( lista interfaces )
# tcpdump -w captura.pcap  ( guarda la captura en fichero captura.pcap )
# tcpdump host IP  ( captura todo lo entra y sale a una IP )
# tcpdump -s0 port 383  ( filta por puerto )
# tcpdump -s0 not port 22 and port 636 ( filtra por puerto y evita captura de otro )
# tcpdump -i eth0 -s0 -w -vvv not port 22 and port 636 -w /tmp/captura.pcap |stdbuf -oL tcpick -C -v -a -h -yP -r 
tcpdump -i eth0 -s0 -vvv not port 22

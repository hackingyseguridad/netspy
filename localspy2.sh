# tshark  -Ttabs -f "udp port 53"
# tshark  -Ttabs -Y "tcp.port !=22"
# tshark  -Ttabs -f "tcp port 8443"  -w captura.pcap
#!/bin/bash
tshark  -Ttabs

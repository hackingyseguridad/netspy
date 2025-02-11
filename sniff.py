#!/usr/bin/env python3
# sniff en python3 para red local

from scapy.all import sniff, IP, TCP, UDP, ICMP, ARP, DNS

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "ICMP" if packet.haslayer(ICMP) else "ARP" if packet.haslayer(ARP) else "DNS" if packet.haslayer(DNS) else "Other"

        print(f"[+] {src_ip} -> {dst_ip} | Protocol: {protocol}")

        # Additional details based on the protocol
        if packet.haslayer(TCP):
            print(f"    TCP Port: {packet[TCP].sport} -> {packet[TCP].dport}")
        elif packet.haslayer(UDP):
            print(f"    UDP Port: {packet[UDP].sport} -> {packet[UDP].dport}")
        elif packet.haslayer(ICMP):
            print(f"    ICMP Type: {packet[ICMP].type} Code: {packet[ICMP].code}")
        elif packet.haslayer(ARP):
            print(f"    ARP Operation: {packet[ARP].op} | Src MAC: {packet[ARP].hwsrc} | Dst MAC: {packet[ARP].hwdst}")
        elif packet.haslayer(DNS):
            print(f"    DNS Query: {packet[DNS].qd.qname} | Type: {packet[DNS].qd.qtype}")

def start_sniffing(interface, filter_exp):
    print(f"[*] Starting  on {interface} with filter '{filter_exp}'...")
    sniff(iface=interface, prn=packet_callback, store=False, filter=filter_exp)

if __name__ == "__main__":
    ascii_art = """
    **************************

    Usp: ython3 sniff.py

    **************************

    """
    print(ascii_art)
    print("sniff.py\n")
    print("")
    print("Menu : ")
    print("1. All Traffic")
    print("2. HTTP Traffic")
    print("3. HTTPS Traffic")
    print("4. TCP Traffic")
    print("5. UDP Traffic")
    print("6. ICMP Traffic")
    print("7. ARP Traffic")
    print("8. DNS Traffic")
    print("9. Custom Filter")

    choice = input("Enter your choice (1-9): ")
    filter_exp = ""

    if choice == "2":
        filter_exp = "tcp port 80"
    elif choice == "3":
        filter_exp = "tcp port 443"
    elif choice == "4":
        filter_exp = "tcp"
    elif choice == "5":
        filter_exp = "udp"
    elif choice == "6":
        filter_exp = "icmp"
    elif choice == "7":
        filter_exp = "arp"
    elif choice == "8":
        filter_exp = "udp port 53"
    elif choice == "9":
        filter_exp = input("Enter a BPF filter expression: ")

    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    start_sniffing(interface, filter_exp)

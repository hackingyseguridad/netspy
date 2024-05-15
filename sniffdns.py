#!/ usr / bin / envidia pitón3
de Scapy. Todas las importaciones *
Definido _ DNS (p):
si p. Haslayer (DNS):
Impresión (p [IP]. src, p [DNS]. resumen)
Sniff (prn=find _ DNS)

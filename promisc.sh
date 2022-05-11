#!/bash/bin
# hackingyseguridad.com 2022
# Poner modo promiscuo interface ethernet para interceptacion
# habilitar promiscuo: ifconfig eth0 promisc
# deshabilitar modo promiscuo: ifconfig eth0 -promisc 
# Cambiar MAC: ifconfig eth0 hw ether aa:bb:cc:11:22:33
ifconfig $1 promisc

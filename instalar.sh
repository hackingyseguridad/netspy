#!/bin/bash
echo
echo "instalando go ..."
sudo apt-get install golang
echo "instalando bettercap ..."
go get github.com/evilsocket/bettercap-ng
echo "fin"

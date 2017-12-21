#! /usr/bin/env python
#
#bodhi wang
#bodwang@deloitte.com.cn
#2017.12.20
import socket
import sys
import os

CLIENT_SOCK="/tmp/client.sock"
SERV_SOCK="/var/run/shadowsocks-manager.sock"
TIMEOUT_SECS=10

if len(sys.argv) < 2:
   print("usage: {0} <command str>".format(sys.argv[0]))
   sys.exit(1)

cmdstr=sys.argv[1]
print("cmdstr[{}]".format(cmdstr))


cli = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
try:
   cli.bind(CLIENT_SOCK)  # address of the client
except Exception as e:
   print("Failed to bind {}:{}".format(CLIENT_SOCK,e.message))
   sys.exit(1)

cli.connect(SERV_SOCK)  # address of Shadowsocks manager
cli.send(cmdstr)

status = 0
try:
   cli.settimeout(TIMEOUT_SECS)
   print(cli.recv(1506))  # You'll receive 'ok'
except Exception as e:
   print("Failed to receive: {}".format(e.message))
   status = 1

cli.close()
os.remove(CLIENT_SOCK)
sys.exit(status)

#!/usr/bin/env python

import sys, socket, string

HOST="192.168.15.24"
PORT=8637

#HOST="irc.rizon.net"
#PORT=6667

s = socket.socket()
s.connect((HOST,PORT))

print "Connected"

while True:
#  try:
#  line = s.recv(500).rstrip()
#  except :
#  if len(line) == 0:
#    exit()

#  print(line)
  s.send(raw_input())

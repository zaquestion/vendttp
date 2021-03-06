#!/usr/bin/env python

import time, socket, threading

HOST="localhost"
PORT=8637

sock = None

def send():
  global sock
  while True:
    message = raw_input()
    try:
      sock.send(message)
    except:
      print "[ERROR] not connected to a server"

def receive():
  global sock
  while True:
    try:
      sock = socket.socket()
      sock.connect((HOST,PORT))
      print "Successfully connected to server"
    except:
      time.sleep(2)
      continue
    while True:
      try:
        message = sock.recv(500).rstrip()
        if len(message) != 0:
          print "from server: " + `message`
        else:
          break
      except:
        break
    print "Disconnected from server"
    sock = None
    
print "Starting bill acceptor client emulator."
print "Attempting to connect to server..."

send_thread = threading.Thread(target=send)
receive_thread = threading.Thread(target=receive)

try:
  receive_thread.start()
  send_thread.run()
except (KeyboardInterrupt, EOFError, SystemExit):
  print "Exiting..."
  receive_thread._Thread__stop()
  send_thread._Thread__stop()
  sys.exit()

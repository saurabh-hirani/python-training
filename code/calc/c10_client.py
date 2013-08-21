import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inputfile = sys.argv[1]
f = open(inputfile, 'r')
s.connect(('127.0.0.1', 9000))
for line in f:
    print "\nclient sending %s" % line
    s.send(line)
    data = s.recv(1024)
    print "server replied %s" % data
f.close()
s.close()

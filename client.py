#!/usr/bin/env python
import sys
import zmq


DEFAULT = '172.16.16.228'


def run(server_ip):
    context = zmq.Context()

    socket = context.socket(zmq.DEALER)

    socket.connect('tcp://%s:5555' % server_ip)

    for i in range(10):
        socket.send_multipart([str(i)])
        socket.recv()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ip = sys.argv[1]
    else:
        print 'using default %s' % DEFAULT
        ip = DEFAULT
    run(ip)

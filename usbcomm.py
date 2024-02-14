import select
import sys
import time

def listen():
    poll_obj = select.poll()
    poll_obj.register(sys.stdin, select.POLLIN)

    while 1:
        poll_results = poll_obj.poll(1)
        if poll_results:
            data = sys.stdin.readline().strip()
            sys.stdout.write("received data: " + data + "\r")
            return data
        else:
            continue

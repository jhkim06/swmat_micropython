import select
import sys
import time

def listen():
    # print("listen")
    poll_obj = select.poll()
    poll_obj.register(sys.stdin, select.POLLIN)

    while 1:
        poll_results = poll_obj.poll(1)
        if poll_results:
            data = sys.stdin.readline().strip()
            sys.stdout.write("Get " + data + " from user.\r")
            return data
        else:
            continue

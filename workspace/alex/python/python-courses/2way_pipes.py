import os, time, sys
pipe_name = 'pipe_test'

def child():
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    while True:
        time.sleep(1)
        os.write(pipeout, 'Number 674335744\n' ����
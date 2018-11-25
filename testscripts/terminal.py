from subprocess import Popen, PIPE
from contextlib import suppress
import time

def execute(command):
    proc = Popen(command, stdin = PIPE, stdout = PIPE, shell = True)
    while proc.poll() is None:
        stdout = proc.stdout.readline().decode()
        print(stdout)
        proc.stdin.write(b'5\n')
        with suppress(Exception):
            proc.stdin.flush()

    stdout = proc.stdout.readline().decode()
    print(stdout[:-1])
        
try:
    Popen(['gcc', 'DisplayN.c']).wait()
    execute('./a.out')
except:
    print('error')
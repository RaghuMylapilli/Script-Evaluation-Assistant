from subprocess import Popen, PIPE
from contextlib import suppress

def execute(command):
    proc = Popen(command, stdin = PIPE, stdout = PIPE, shell = True)
    while proc.poll() is None:
        stdout = proc.stdout.readline().decode()
        print(stdout)
        proc.stdin.write(b'10\n')
        with suppress(Exception):
            proc.stdin.flush()


    stdout = proc.stdout.readline().decode()
    print(stdout)
        
execute('./a.out')
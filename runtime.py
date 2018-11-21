from subprocess import run, PIPE, Popen
from contextlib import suppress
import time
import os

separator = "/"
if os.name == 'nt':
    separator = "\\"

def static_execute(script, runtime, path, input_data):
    '''
    :param script: A string with the script to be executed
    :param path: A string og the path in which the script is present
    :param input_data: A string of the data to be passed as input to the script
    :return: 0 if exec successfully, 1 if not.

    Executes the given script as a seperate subprocess and stores its output in a file
    The inputs are given in advance and collected after the process finishes execution
    '''
    file = open(path + separator + 'op.txt', 'r+')
    file.truncate(0)
    file.close()

    with open(path + '/op.txt', 'w') as output_file:
        start = time.time()
        status = run([runtime, script],
                                cwd=path,
                                input=input_data,
                                encoding='ascii',
                                stdout=output_file)
        stop = time.time()
        output_file.write('Time Taken: ' + str(stop - start) + 's\n')
    return status.returncode

def dynamic_execute(command, path, output):
    '''
    :param command: string, command to be executed
    :param path: the path in which the exec file is present
    :param output: the output var to set outputs
    :return: None

    Dynamically interacts with the program using PIPE
    '''
    proc = Popen(command,
                 cwd = path,
                 stdin = PIPE,
                 stdout = PIPE,
                 shell = True)
    while proc.poll() is None:
        stdout = proc.stdout.readline().decode()
        print(stdout)
        proc.stdin.write(b'10\n')
        with suppress(Exception):
            proc.stdin.flush()


    stdout = proc.stdout.readline().decode()
    print(stdout)
import subprocess
import time

def execute(script, path, input_data):
    '''
    execute(script, path, input_data
    :param script: A string with the script to be executed
    :param path: A string og the path in which the script is present
    :param input_data: A string of the data to be passed as input to the script
    :return: 0 if exec successfully, 1 if not.

    Executes the given script as a seperate subprocess and stores its output in a file
    '''
    file = open(path + '/op.txt', 'r+')
    file.truncate(0)
    file.close()

    with open(path + '/op.txt', 'w') as output_file:
        start = time.time()
        status = subprocess.run(['python3', script],
                                cwd=path,
                                input=input_data,
                                encoding='ascii',
                                stdout=output_file)
        stop = time.time()
        output_file.write('Time Taken: ' + str(stop - start) + '\n\n')

    return status.returncode
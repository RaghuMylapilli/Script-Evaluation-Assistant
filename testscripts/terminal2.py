import subprocess
def main():
    proc = subprocess.Popen('./a.out',
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    # To avoid deadlocks: careful to: add \n to output, flush output, use
    # readline() rather than read()
    proc.stdin.write(b'2+2\n')
    proc.stdin.flush()
    print(proc.stdout.readline())

    proc.stdin.write(b'len("foobar")\n')
    proc.stdin.flush()
    print(proc.stdout.readline())

    proc.stdin.close()
    proc.terminate()
    proc.wait(timeout=0.2)

main()
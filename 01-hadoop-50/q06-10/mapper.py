import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__": 
    for line in sys.stdin:
        
        lines=line.split()
        sys.stdout.write('{}\t{}\n'.format(lines[0],lines[2]))

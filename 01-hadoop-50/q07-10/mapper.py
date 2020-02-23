import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__": 
    for line in sys.stdin:
        
        lines=line.split()
        clave=lines[0]+lines[2]
        sys.stdout.write('{};{};{};{}\n'.format(clave,lines[0],lines[1],lines[2]))
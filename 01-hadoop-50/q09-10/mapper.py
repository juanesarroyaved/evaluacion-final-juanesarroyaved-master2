import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
for line in sys.stdin:
    
    lines=line.split()
    
    sys.stdout.write('{}\t{}\t{}\n'.format(lines[2],lines[1],lines[0]))
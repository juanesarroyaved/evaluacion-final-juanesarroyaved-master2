import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__": 

    for line in sys.stdin:
        lines=line.split()
        word= lines[1].split('-')
        sys.stdout.write('{}\t1\n'.format(word[1]))
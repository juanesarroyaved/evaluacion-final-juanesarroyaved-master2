import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':


    for line in sys.stdin:
        clave,key,nada,val = line.split(";")
        val = int(val)
        
        sys.stdout.write("{}\t{}\t{}\n".format(key,nada,val))
import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':
    curkey = None
    valor = []
    lines = sys.stdin.readlines()

    for line in lines:
        key, val = line.split("\t")
        val=int(val.replace('\n',''))
               
        if key == curkey:
            valor.append(val)
        else:
            if curkey is not None:

                valor.sort()
                valor=','.join(str(x) for x in valor)
                sys.stdout.write("{}\t{}\n".format(curkey,valor)) 
            
            curkey = key
            valor=[val]

    if key == curkey:

        valor.sort()
        valor=','.join(str(x) for x in valor)
        sys.stdout.write("{}\t{}\n".format(curkey, valor))
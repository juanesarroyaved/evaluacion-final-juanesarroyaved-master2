import sys
#
#  >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':
    curkey = None
    total = []
    for line in sys.stdin:
        key, val = line.split(";")
        val = int(val)
        if key == curkey:
            total.append(val)
        else:
            if curkey is not None:
                maxi = max(total)
                sys.stdout.write("{}\t{}\n".format(curkey,maxi))
            curkey = key
            total = []
    maxi = max(total)
    sys.stdout.write("{}\t{}\n".format(curkey,maxi))
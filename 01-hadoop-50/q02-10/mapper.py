import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    prop=''
    monto=0
    for line in sys.stdin:
        line = line.strip()
        splits = line.split(",")
        prop = splits[3]
        monto = int(splits[4])
        sys.stdout.write("{};{}\n".format(prop,monto))
import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':
    col2 = ''
    col1 = 0
    for line in sys.stdin:
        line = line.strip()
        splits = line.split(";")
        col2 = splits[1]
        col1 = int(splits[0])
        sys.stdout.write("{},{}\n".format(col2,col1))
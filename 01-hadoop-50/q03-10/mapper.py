import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    col1 = ''
    col2 = 0
    for line in sys.stdin:
        line = line.strip()
        splits = line.split(",")
        col1 = splits[0]
        col2 = int(splits[1])
        sys.stdout.write("{};{}\n".format(col2,col1))
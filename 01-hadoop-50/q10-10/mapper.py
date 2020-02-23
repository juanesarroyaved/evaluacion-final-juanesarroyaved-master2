import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
 
if __name__ == "__main__": 
    lines = sys.stdin.readlines()

    for line in lines:
        key=line.split('\t')[0]
        letter=line.split('\t')[1].replace('\n','').replace(',','').replace(' ','')
        letter=letter.strip()
        for word in letter:
            sys.stdout.write("{}\t{}\n".format(word,str(key)))       
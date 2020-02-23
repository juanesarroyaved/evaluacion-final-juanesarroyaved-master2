import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
total=[]

for line in sys.stdin:
    line = line.strip()
    val,nada,letra = line.split("\t") 
    val = int(val)
    
    x=(letra,nada,val)
    total.append(x)

total.sort(key=lambda x: x[2])

for l in range(6):
    
    letra,nada,val=total[l]
    sys.stdout.write("{}\t{}\t{}\n".format(letra,nada,val))
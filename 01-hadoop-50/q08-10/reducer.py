import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
curkey = None
total = 0
contador=0

for line in sys.stdin:
        
    key, val = line.split("\t") 
    val = float(val)
    
    if key == curkey:      
        total += val
        contador = contador + 1 
        
    else:
        if curkey is not None:
                
            sys.stdout.write("{}\t{}\t{}\n".format(curkey,total,float(total/contador)))
            contador=1
            total=val
            curkey=key
   
        else:
            curkey = key
            total=val
            contador=1
               
sys.stdout.write("{}\t{}\t{}\n".format(curkey,total,float(total/contador)))
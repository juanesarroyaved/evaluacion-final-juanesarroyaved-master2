import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__': 
    
    curkey = None
    total = []

    for line in sys.stdin:
        key, val = line.split("\t") 
        val = float(val)
        
        if key == curkey: 
            total.append(val)
                 
        else:
            
            if curkey is not None:
                Maxi=max(total)
                Mini=min(total)
                sys.stdout.write("{}\t{}\t{}\n".format(curkey,Maxi,Mini))

            
            curkey = key
            total = []
            total.append(val)
    
    Maxi=max(total)
    Mini=min(total)
    sys.stdout.write("{}\t{}\t{}\n".format(curkey,Maxi,Mini))
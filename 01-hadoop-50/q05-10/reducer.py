import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
curkey = None
total = 0

for line in sys.stdin:
        
    key, val = line.split("\t") 
    val = int(val)
        
    if key == curkey: 
            
        total += val
            
    else:

        if curkey is not None:

            sys.stdout.write("{}\t{}\n".format(curkey, total)) 
            
        curkey = key
        total = val
            
sys.stdout.write("{}\t{}\n".format(curkey, total)) 

import argparse
parser = argparse.ArgumentParser(description='Process some numbers.')

final = 1;

while True:
    try:
        standInput = raw_input()
    except EOFError:
        print "^D"
        break
        
    if standInput == "":
        print final
    else:      
        try:
            float(standInput)
        except ValueError:
            print 'could nto conver string to float: ' + standInput
            import sys
            sys.exit(1)
    
    if standInput != "":     
        final *= int(standInput)
    
print final

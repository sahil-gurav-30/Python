import time
import sys
print("Name   : Sahil Gurav")
print("USN    : 1AY24AI093")
print("Section: O\n")
indent = 0     
indent_increasing = True
try:
    while True:
        print(' ' * indent + '*' * 10)  
        time.sleep(0.1)  # Pause for 0.1 seconds
        if indent_increasing:
            indent += 1
            if indent == 20: 
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit() 

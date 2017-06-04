# Erin Cole
# Main fucntion for VIS141A Project1


import sys
import time
import drawShapes

# This function handles all print statements and function calls.  It creates
# a narritive for the user to read, and (hopefully) evokes feelings of 
# frustration
if __name__ == '__main__':
    shortPause = 2
    longPause = 5
    i = 1
    # Print initial greeting
    sys.stdout.write("Let's have fun with shapes!\n\n")
    sys.stdout.flush()
    time.sleep(shortPause)

    sys.stdout.write("I will make you a circle: \n\n")
    sys.stdout.flush()
    time.sleep(longPause)

    # Make a square instead of a circle
    drawShapes.makeSquare()
    time.sleep(shortPause)

    sys.stdout.write("Wait... I made the wrong thing.\n\n")
    sys.stdout.flush()
    time.sleep(shortPause)
    
    while i < 4:
        sys.stdout.write(".\n\n")
        sys.stdout.flush()
        time.sleep(shortPause)
        i = i + 1
 
    sys.stdout.write("Let me try again.\n\n")
    sys.stdout.flush()
    time.sleep(longPause)

    # Make either a circle or a square
    drawShapes.randomize()
    time.sleep(shortPause)

    sys.stdout.write("Sometimes I'm right, sometimes I'm wrong.\n\n")
    sys.stdout.flush()
    time.sleep(shortPause)

    # Make another randomized shape
    drawShapes.randomize()
    time.sleep(shortPause)

    sys.stdout.write("OOPS!!! Sometimes I just make mistakes.\n")
    sys.stdout.write("Didn't mean to make that one!\n\n")

    sys.stdout.flush()
    time.sleep(shortPause)

    # Make a few randomized shapes
    i = 1
    while i < 4:
        drawShapes.randomize()
        i = i + 1

    sys.stdout.write("Those I meant to make.\n")
    sys.stdout.flush()
    time.sleep(longPause)
    
    # Program gets snarky
    sys.stdout.write("Looks like you have some cleaning to do...\n\n")
    sys.stdout.flush()
    time.sleep(shortPause)

    i = 1
    while i < 4:
        sys.stdout.write(".\n\n")
        sys.stdout.flush()
        time.sleep(shortPause)
        i = i + 1

    # Closing statement
    sys.stdout.write("I'm done. Bye!\n\n")
    sys.stdout.flush()
    time.sleep(longPause)

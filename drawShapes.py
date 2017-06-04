# Erin Cole
# This program contains the functions that draw different shapes, when called.

from PIL import Image
from Lib import random
import time


# Function name: randomize
# This function will randomly make either a circle or a square, in accordance
# with a random seed
def randomize():
    randVal = random.random()

    if randVal < .5:
        makeCircle()
    
    else:
        makeSquare()

# Function name: makesquare
# This function will show a square.jpg file
def makeSquare():
    square = Image.open('square.jpg')
    square.show()


# Function name: makeCircle
# This function will show a circle.jpg file
def makeCircle():
    circle = Image.open('circle.jpg')
    circle.show()

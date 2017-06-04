from PIL import Image
from Lib import random
import time

def randomize():
    randVal = random.random()

    if randVal < .5:
        makeCircle()
    
    else:
        makeSquare()

def makeSquare():
    square = Image.open('square.jpg')
    square.show()


def makeCircle():
    circle = Image.open('circle.jpg')
    circle.show()

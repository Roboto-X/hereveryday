from PIL import Image
import numpy as np
import os



def predo(filename):
    im = Image.open(filename)
    out = im.resize((28, 28),Image.ANTIALIAS)
    out.save('resized/' + filename, "JPEG")

predo(filename='image.png')

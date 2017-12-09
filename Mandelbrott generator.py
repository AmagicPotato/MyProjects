from PIL import Image
from numba import jit
import math

xmin = -1.5
xmax = 0.5
ymin = -1.1
ymax = 1.1

width = 500
height = 500

minimumcontrast = 0.20

img = Image.new('RGB', (width,height), "black")
pixels = img.load()

@jit
def check(a,b):

    real = 0
    imagine = 0

    divergent = 0

    n = 0

    while(n < 50):

        a_hold =  (real**2 - imagine**2) + a
        b_hold = (2*real*imagine) + b

        real = a_hold
        imagine = b_hold

        if( math.sqrt(real**2 + imagine**2) > 2 ):
            divergent = minimumcontrast + (1 - minimumcontrast)/(n+1)
            break

        n += 1

    return divergent

lastpercent = 0

for i in range(img.size[0]):    # for every col:
    percentage = int(i/img.size[0] * 100)
    
    if percentage != lastpercent:
        print(str(percentage) + "%")

    lastpercent = percentage
    for j in range(img.size[1]):    # For every row
        re = xmin + (((xmax - xmin) / width) * i) 
        im = ymin + (((ymax - ymin) / width) * j) 
        mandel = check(re,im)
        pixels[i,j] = (int(256 * mandel), int(256 * mandel), int(256 * mandel)) # set the colour accordingly

img.show()

#!/bin/python3
import sys 
import cv2
import numpy as np

def RBG2GRAY(img):
    r,b,g = img[:,:,0],img[:,:,1],img[:,:,2]
    return 0.3*r + 0.59*b + 0.11*g

def main(args):
    inputfile = ''
    outputfile = ''
    for i in range(len(args)):
        if args[i] == '-input':
            inputfile = args[i+1]
        if args[i] == '-output':
            outputfile= args[i+1]
    image = cv2.imread(inputfile, cv2.IMREAD_COLOR)
    gray = RBG2GRAY(image)
    cv2.imwrite(outputfile,gray)


if __name__ == '__main__':
    print("Welcome to cover RGB to gray")
    main(sys.argv)
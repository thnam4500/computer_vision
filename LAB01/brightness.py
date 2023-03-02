#!/bin/python3
import sys 
import cv2
import numpy as np

def ChangeBrightNess(img,brightnessFactor):
    img = img + brightnessFactor
    img[img > 255] = 255
    return img

def main(args):
    inputfile = ''
    outputfile = ''
    brightness = 0
    for i in range(len(args)):
        if args[i] == '-input':
            inputfile = args[i+1]
        if args[i] == '-output':
            outputfile= args[i+1]
        if args[i] == '-brightness':
            brightness = float(args[i+1])
    image = cv2.imread(inputfile, cv2.IMREAD_COLOR)
    new_image = ChangeBrightNess(image,brightness)
    cv2.imwrite(outputfile,new_image)
    


if __name__ == '__main__':
    print("Welcome to change brightness")
    main(sys.argv)
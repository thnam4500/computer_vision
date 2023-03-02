#!/bin/python3
import sys 
import cv2
import numpy as np

def ChangeContrast(img,factor):
    img = img * factor
    img[img < 128] = img[img < 128]/factor
    img[img > 128] = img[img > 128]*factor
    img[img < 0] = 0
    img[img > 255] = 255
    return img

def main(args):
    inputfile = ''
    outputfile = ''
    contrast = 0
    for i in range(len(args)):
        if args[i] == '-input':
            inputfile = args[i+1]
        if args[i] == '-output':
            outputfile= args[i+1]
        if args[i] == '-contrast':
            contrast = float(args[i+1])
    image = cv2.imread(inputfile, cv2.IMREAD_COLOR)
    new_image = ChangeContrast(image,contrast)
    cv2.imwrite(outputfile,new_image)
    


if __name__ == '__main__':
    main(sys.argv)
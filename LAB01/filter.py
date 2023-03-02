#!/bin/python3
import sys 
import cv2
import numpy as np

def Filter(img,kernel):
    return img

def GetKernel(kernelType,kernelSize):
    if kernelType == 'avg':
        kernel = np.ones([kernelSize,kernelSize])
        return kernel/(kernelSize**2)

def main(args):
    inputfile = 'image.png'
    outputfile = 'result.png'
    kernelSize = 0
    filterType = 'avg'
    for i in range(len(args)):
        if args[i] == '-input':
            inputfile = args[i+1]
        if args[i] == '-output':
            outputfile= args[i+1]
        if args[i] == '-size':
            kernelSize = int(args[i+1])
        if args[i] == '-filter':
            filterType = args[i+1]
    image = cv2.imread(inputfile, cv2.IMREAD_COLOR)
    kernel = GetKernel(filterType,kernelSize)
    new_image = Filter(image,kernel)
    cv2.imwrite(outputfile,new_image)
    


if __name__ == '__main__':
    main(sys.argv)